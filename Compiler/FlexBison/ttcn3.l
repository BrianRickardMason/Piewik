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

void atBegin(YYLTYPE* aLocation, int aLen) {
    aLocation->step();
    aLocation->columns(aLen);
}

void onNewLine(YYLTYPE* aLocation) {
    aLocation->lines(1);
}

typedef Ttcn3BisonParser::parser::token TOKEN_TYPE;

%}

Lexer_AlphaNumUnder     [A-Za-z0-9_]
Lexer_Alpha             [A-Za-z]
    /* REF(RULE TODO) */
Lexer_Num               [0-9]
    /* REF(RULE TODO) */
Lexer_NonZeroNum        [1-9]
    /* REF(RULE 419) */ 
Lexer_Number            {Lexer_NonZeroNum}{Lexer_Num}*|"0"
    /* REF(RULE 424) */
Lexer_Bin               [01]
    /* REF(RULE TODO) */
Lexer_Hex               [0-9a-fA-F]
    /* REF(RULE TODO) */
Lexer_Oct               [0-9a-fA-F]{2}
Lexer_WHITESPACE        [\n\t ]
Lexer_NEWLINE           [\n]
    /* REF(RULE 436) */
    /* REFERENCE - A graphical character from the BASIC LATIN or from the LATIN-1 SUPPLEMENT character sets defined in ISO/IEC 10646 (characters from char (0,0,0,32) to char (0,0,0,126), from char (0,0,0,161) to char (0,0,0,172) and from char (0,0,0,174) to char (0,0,0,255) */
Lexer_ExtendedAlphaNum [\x20-\x7E\xA1-\xAC\xAE-\xFF]

%x IN_BLOCK_COMMENT
%x IN_LINE_COMMENT

%%
    /* Comments */
"/*" {
    atBegin(yylloc, yyleng);
	BEGIN(IN_BLOCK_COMMENT);
    
    //return Ttcn3BisonParser::parser::token::COMMENT_START;
}

<IN_BLOCK_COMMENT>"*/" {
    atBegin(yylloc, yyleng);
	BEGIN(INITIAL);
    std::string comment(yytext, yytext + yyleng-2);
    std::clog <<"comment was: " << comment << std::endl;
    //return Ttcn3BisonParser::parser::token::COMMENT_END;
}

<IN_BLOCK_COMMENT>[^\*\n]* {
    atBegin(yylloc, yyleng);
    yymore();
}

<IN_BLOCK_COMMENT>\* {
    atBegin(yylloc, yyleng);
    yymore();
}

<IN_BLOCK_COMMENT>\n {
    atBegin(yylloc, yyleng);
    onNewLine(yylloc);
    yymore();
}

"//" {
    atBegin(yylloc, yyleng);
    BEGIN(IN_LINE_COMMENT);
    //return Ttcn3BisonParser::parser::token::COMMENT_START;
}

<IN_LINE_COMMENT>[^\n]* {
    atBegin(yylloc, yyleng);
    std::string comment(yytext, yytext + yyleng);
    std::clog <<"comment was: " << comment << std::endl;
    //return Ttcn3BisonParser::parser::token::COMMENT_BODY;
}

<IN_LINE_COMMENT>{Lexer_NEWLINE} {
    atBegin(yylloc, yyleng);
    onNewLine(yylloc);
    BEGIN(INITIAL);
    //return Ttcn3BisonParser::parser::token::COMMENT_END;
}

    /* Spaces */

{Lexer_NEWLINE} { 
    atBegin(yylloc, yyleng);
    onNewLine(yylloc);
}

{Lexer_WHITESPACE} { 
    atBegin(yylloc, yyleng); 
}

    /* Keywords */

    /* REF(RULE 2) */
"module" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::TTCN3ModuleKeyword;
}
    /* REF(RULE 4) */
"language" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::LanguageKeyword;
}
    /* REF(RULE 82) */
"const" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::ConstKeyword;
}

    /* REF(RULE 390) */
"bitstring" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::BitStringKeyword;
}
    /* REF(RULE 391) */
"boolean" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::BooleanKeyword;
}
    /* REF(RULE 392) */
"integer" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::IntegerKeyword;
}
    /* REF(RULE 393) */
"octetstring" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::OctetStringKeyword;
}
    /* REF(RULE 394) */
"hexstring" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::HexStringKeyword;
}
    /* REF(RULE 395) */
"verdicttype" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::VerdictTypeKeyword;
}
    /* REF(RULE 396) */
"float" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::FloatKeyword;
}
    /* REF(RULE 397) */
"address" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::AddressKeyword;
}
    /* REF(RULE 398) */
"default" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::DefaultKeyword;
}
    /* REF(RULE 399) */
"anytype" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::AnyTypeKeyword;
}
    /* REF(RULE 400) */
"charstring" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::CharStringKeyword;
}
    /* REF(RULE 402) */
"universal" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::UniversalKeyword;
}

    /* REF(RULE 412) */
"char" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::CharKeyword;
}
    /* REF(RULE 414) */
"not_a_number" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::NaNKeyword;
}
    /* REF(RULE 439) */
"omit" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::OmitKeyword;
}

    /* REF(RULE 438) */
"null" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::AddressValue;
}

    /* REF(RULE 408) */
("true"|"false") {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::BooleanValue;
}
    /* REF(RULE 409) */ 
("pass"|"fail"|"inconc"|"none"|"error") {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::VerdictTypeValue;
}

    /* REF(RULE 415) */
{Lexer_Number}\.{Lexer_Num}+ {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::FloatDotNotation;
}

    /* REF(RULE 416) FloatENotation ::= Number [Dot DecimalNumber] Exponential [Minus] Number */
{Lexer_Number}(\.{Lexer_Num}+)?E\-?{Lexer_Number} {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::FloatENotation;
}


    /* REF(RULE 417) */ 
"E" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Exponential;
}

    /* REF(RULE 419) */ 
{Lexer_Number} {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Number;
}

    /* REF(RULE 421) */ 
{Lexer_Num}+ {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::DecimalNumber;
}

    /* REF(RULE 423) Bstring ::= "'" {Bin} "'" "B" */
\'{Lexer_Bin}*\'B {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Bstring;
}

    /* REF(RULE 425) Hstring ::= "'" {Hex} "'" "H" */
\'{Lexer_Hex}*\'H {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Hstring;
}

    /* REF(RULE 427) Ostring ::= "'" {Oct} "'" "O" */
\'{Lexer_Oct}*\'O {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Ostring;
}

    /* REF(RULE 429) Cstring ::= """ {Char} """ */
    /* 430.Char ::= */
    /* REFERENCE - A character defined by the relevant CharacterString type. For charstring a character from the character set defined in ITU-T T.50. For universal charstring a character from any character set defined in ISO/IEC 10646 */
\"([^"]|\"\")*\" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Cstring;
}

    /* REF(RULE 431) Identifier ::= Alpha {AlphaNum | Underscore} */
{Lexer_Alpha}{Lexer_AlphaNumUnder}* {
    atBegin(yylloc, yyleng);
    return Ttcn3BisonParser::parser::token::Identifier;
}

    /* REF(RULE 437) FreeText ::= """ {ExtendedAlphaNum} """ */
\"{Lexer_ExtendedAlphaNum}*\" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::FreeText;
}

    /* REF(RULE 560) */
"." {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Dot;
}

    /* REF(RULE 561) */
"-" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Minus;
}

    /* REF(RULE 562) */
";" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::SemiColon;
}

    /* REF(RULE 563) */
":" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Colon;
}

    /* REF(RULE 564) */
"_" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::Underscore;
}

    /* REF(RULE 565) */
":=" {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::AssignmentChar;
}

".." {
    atBegin(yylloc, yyleng);
    return TOKEN_TYPE::DoubleDot;
}

("["|"]"|"{"|"}"|"("|")"|",") {
    atBegin(yylloc, yyleng);
    // these are ok, but used explicit in the grammar
    return static_cast<int>(yytext[0]);
}

. {
    atBegin(yylloc, yyleng);
    return Ttcn3BisonParser::parser::token::UNEXPECTED;
}

<<EOF>> {
    yyterminate();
}

%%
