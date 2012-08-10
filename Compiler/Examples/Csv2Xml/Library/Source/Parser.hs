{-# LANGUAGE FlexibleContexts #-}

module Parser where

import Prelude

import Text.Parsec
import Text.Parsec.Char
import Text.Parsec.Combinator

-- CSV file grammar
-- ------
-- file         ::= [ header ] { line }
-- comment      ::= # { character* }
-- header       ::= [ line | lastLine ]
-- line         ::= [ entry { separator entry } ] newline
-- lastLine     ::= [ entry { separator entry } ]
-- entry        ::= alphanum+ | " { character* } "
-- newline      ::= \n
-- separator    ::= ,
-- alphanum     ::= a|b|..|A|B|..|0|1|..
-- character    ::= alphaNum|newline|separator|""

csvP :: (Stream s m Char) => ParsecT s u m [[String]]
csvP =
    do header <- option [] (try lineP)
       lines <- option [] (many $ commentP <|> try lineP)
       lastLine <- option [] lastLineP
       eof
       return $! filter (not . null) ((header : lines) ++ (lastLine : []))

commentP :: (Stream s m Char) => ParsecT s u m [String]
commentP =
    startCommentP >> skipMany (noneOf "\n") >> (return [])
    where
        startCommentP :: (Stream s m Char) => ParsecT s u m Char
        startCommentP = (char '#')

lineP :: (Stream s m Char) => ParsecT s u m [String]
lineP =
    do entry <- option [] (entryP `sepBy` separatorP)
       newlineP
       return entry

lastLineP :: (Stream s m Char) => ParsecT s u m [String]
lastLineP = option [] (entryP `sepBy` separatorP)

entryP :: (Stream s m Char) => ParsecT s u m String
entryP = manyAlphaNumP <|> manyQuotedCharacterP
    where
        manyAlphaNumP = many1 alphaNumP
        manyQuotedCharacterP =
            do quoteP
               content <- many (characterP <|> doubleQuoteP)
               quoteP

               return content

alphaNumP :: (Stream s m Char) => ParsecT s u m Char
alphaNumP = alphaNum

characterP :: (Stream s m Char) => ParsecT s u m Char
characterP = 
    oneOf $ ['a'..'z'] ++ 
            ['A'..'Z'] ++ 
            ['0'..'9'] ++ 
            [',','\n']

quoteP :: (Stream s m Char) => ParsecT s u m Char
quoteP = (char '"')

doubleQuoteP :: (Stream s m Char) => ParsecT s u m Char
doubleQuoteP = 
   try $ quoteP >> 
         quoteP >> 
         (return '"')

newlineP :: (Stream s m Char) => ParsecT s u m Char
newlineP = newline

separatorP :: (Stream s m Char) => ParsecT s u m Char
separatorP = 
    spacesP >>
    (char ',') >> 
    spacesP >>
    (return ',')
    where
        spacesP :: (Stream s m Char) => ParsecT s u m ()
        spacesP = skipMany (oneOf " \t")
