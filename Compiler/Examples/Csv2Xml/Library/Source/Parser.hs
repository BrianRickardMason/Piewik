{-# LANGUAGE FlexibleContexts #-}

module Parser where

import Prelude

import Text.Parsec
import Text.Parsec.Char
import Text.Parsec.Combinator

-- CSV file grammar
-- ------
-- file         ::= [ header ] { line }
-- header       ::= [ entry { separator entry } ] newline
-- line         ::= [ entry { separator entry } ] newline
-- entry        ::= alphanum+ | " { character* } "
-- newline      ::= \n
-- separator    ::= ,
-- alphanum     ::= a|b|..|A|B|..|0|1|..
-- character    ::= alphaNum|newline|separator|""

csvP :: (Stream s m Char) => ParsecT s u m [[String]]
csvP =
    do header <- option [] lineP
       lines <- many lineP
       eof
       return (header : lines)

lineP :: (Stream s m Char) => ParsecT s u m [String]
lineP = 
    do entry <- option [] (entryP `sepBy` separatorP)
       newlineP; 
       return entry

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
separatorP = (char ',')
