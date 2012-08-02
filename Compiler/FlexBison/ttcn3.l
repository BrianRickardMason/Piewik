/* %option prefix="Ttcn3" */
%option outfile="Ttcn3Lexer.cpp" header-file="Ttcn3Lexer.h"
%option noyywrap
%option yylineno

%option bison-bridge
%option bison-locations


%{
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>

#include "Ttcn3BisonParser.h"

%}

Lexer_IDENTIFIER_CHAR   [A-Za-z0-9_]
Lexer_IDENTIFIER_START  [A-Za-z]
Lexer_NUMBER            [0-9]
Lexer_WHITESPACE        [\n\t ]
Lexer_NEWLINE           [\n]

%x IN_COMMENT

%%

"/*" {
	BEGIN(IN_COMMENT);{yylloc->step(); yylloc->columns(yyleng);}
    
    //return Ttcn3BisonParser::parser::token::COMMENT_START;
}

<IN_COMMENT>"*/" {
	BEGIN(INITIAL);{yylloc->step(); yylloc->columns(yyleng);}
    //return Ttcn3BisonParser::parser::token::COMMENT_END;
}

<IN_COMMENT>.* {
    {yylloc->step(); yylloc->columns(yyleng);}
    //return Ttcn3BisonParser::parser::token::COMMENT_BODY;
}

{Lexer_NEWLINE} { {yylloc->step(); yylloc->columns(yyleng);} yylloc->lines(1); }
{Lexer_WHITESPACE} { {yylloc->step(); yylloc->columns(yyleng);} }

"_" {
    {yylloc->step(); yylloc->columns(yyleng);}
    return Ttcn3BisonParser::parser::token::UNDERSCORE;
}

{Lexer_NUMBER}+ {
    {yylloc->step(); yylloc->columns(yyleng);}
    return Ttcn3BisonParser::parser::token::INTEGER_CONSTANT;
}

{Lexer_NUMBER}+.{Lexer_NUMBER}+ {
    {yylloc->step(); yylloc->columns(yyleng);}
    return Ttcn3BisonParser::parser::token::FLOAT_CONSTANT;
}

{Lexer_IDENTIFIER_START}{Lexer_IDENTIFIER_CHAR}* {
    {yylloc->step(); yylloc->columns(yyleng);}
    return Ttcn3BisonParser::parser::token::IDENTIFIER;
}

<<EOF>> {
    yyterminate();
}

%%
