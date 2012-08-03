

%file-prefix "Ttcn3"
%output "Ttcn3BisonParser.cpp"
%defines "Ttcn3BisonParser.h"
%language "C++"
%locations
%define namespace Ttcn3BisonParser

%pure-parser
%pure_parser
/* %define api.pure true */


%{
    #include <iostream>
    #include <fstream>
    #include <cstdlib>

    using std::clog;
    using std::endl;
%}

%code requires {
    #include "location.hh"

    #define YYSTYPE void*
    #define YYLTYPE Ttcn3BisonParser::location
    
    #define YYPARSE_PARAM scanner
    #define YYLEX_PARAM   scanner
}

%code top {
    #include "Ttcn3BisonParser.h"
    #include "Ttcn3Lexer.h"
}

%token COMMENT_START COMMENT_END COMMENT_BODY
%token UNEXPECTED
%token Identifier 
%token Number BooleanValue Ostring Hstring Bstring Cstring VerdictTypeValue AddressValue DecimalNumber Exponential FloatDotNotation FloatENotation

%token FreeText
%token Dot Minus SemiColon Colon Underscore AssignmentChar DoubleDot

/** keywords 
 *  naming convention as in the BNF provided in TTCN3 core language document 
 *  definitions in lexer
 */
%token TTCN3ModuleKeyword
%token LanguageKeyword
%token ConstKeyword
%token CharKeyword NaNKeyword
%token BitStringKeyword HexStringKeyword CharStringKeyword OctetStringKeyword UniversalKeyword
%token BooleanKeyword IntegerKeyword FloatKeyword VerdictTypeKeyword
%token AnyTypeKeyword AddressKeyword DefaultKeyword OmitKeyword

%start TTCN3Module

%%  /* Grammar */

/* REF(RULE 1) */
TTCN3Module 
    :	TTCN3ModuleKeyword ModuleId '{' 
            ModuleDefinitionsList
            /*ModuleControlPart TODO */ 
        '}' /*[WithStatement] [SemiColon] TODO */ {
        clog << "Hai" << endl;
    }

/* REF(RULE 3) */
ModuleId
    :   Identifier LanguageSpec {}
    |   Identifier {}

/* REF(RULE 4) */
LanguageSpec 
    :   LanguageKeyword FreeTextList

/* REF(RULE 4) no direct optionals */
FreeTextList
    :   FreeText {}
    |   FreeTextList ',' FreeText {}

/* REF(RULE 6) */
ModuleDefinitionsList 
    :   ModuleDefinitionsListItem {}
    |   ModuleDefinitionsList ModuleDefinitionsListItem {}
    
ModuleDefinitionsListItem
    :   ModuleDefinition SemiColon {}
    |   ModuleDefinition {}  
/* REF(RULE 7) TODO */
/*
ModuleDefinition ::= (([Visibility] (TypeDef |
ConstDef |
TemplateDef |
ModuleParDef |
FunctionDef |
SignatureDef |
TestcaseDef |
AltstepDef |
ImportDef |
ExtFunctionDef |
ExtConstDef
)) |
(["public"] GroupDef) |
(["private"] FriendModuleDef)
) [WithStatement]
*/

ModuleDefinition
    :   ConstDef {}
    
/*ModuleControlPart*/

/* REF(RULE 74) ComponentType ::= ExtendedIdentifier */
ComponentType 
    :   ExtendedIdentifier

/* A.1.6.1.2 Constant definitions */
/* REF(RULE 79) */
ConstDef 
    :   ConstKeyword Type ConstList
/* REF(RULE 80) ConstList ::= SingleConstDef {',' SingleConstDef} */
ConstList 
    :   SingleConstDef 
    |   ConstList ',' SingleConstDef
    
/* REF(RULE 81) SingleConstDef ::= Identifier [ArrayDef] AssignmentChar ConstantExpression */
SingleConstDef 
    :   Identifier ArrayDef AssignmentChar ConstantExpression
    |   Identifier AssignmentChar ConstantExpression

/* STATIC SEMANTICS - Identifier in ParRef shall be a formal parameter identifier from the
associated signature definition */
/* REF(RULE 99) */
ArrayOrBitRef :
    '[' FieldOrBitNumber ']'

/* STATIC SEMANTICS - ArrayRef shall be optionally used for array types and TTCN-3 record of and set
of. The same notation can be used for a Bit reference inside an TTCN-3 charstring, universal
charstring, bitstring, octetstring and hexstring type */
/* REF(RULE 100) */
FieldOrBitNumber 
    :  SingleExpression

/* A.1.6.5 Type */
/* REF(RULE 388) Type ::= PredefinedType | ReferencedType */
Type 
    :   PredefinedType 
    |   ReferencedType

/* REF(RULE 389) */
PredefinedType 
    :   BitStringKeyword 
    |   BooleanKeyword 
    |   CharStringKeyword 
    |   UniversalCharString 
    |   IntegerKeyword 
    |   OctetStringKeyword 
    |   HexStringKeyword 
    |   VerdictTypeKeyword 
    |   FloatKeyword 
    |   AddressKeyword 
    |   DefaultKeyword 
    |   AnyTypeKeyword

/* REF(RULE 401) */
UniversalCharString 
    :   UniversalKeyword CharStringKeyword

/* REF(RULE 403) */
ReferencedType  
    :   ExtendedIdentifier ExtendedFieldReference
    |   ExtendedIdentifier
    
/* REF(RULE 404) */
TypeReference 
    :   Identifier
    
/* REF(RULE 405) ArrayDef ::= {'[' SingleExpression [".." SingleExpression] ']'}+ */
ArrayDefItem
    :   '[' SingleExpression DoubleDot SingleExpression ']'
    |   '[' SingleExpression ']'
    
ArrayDef
    :   ArrayDefItem
    |   ArrayDef ArrayDefItem

/* REF(RULE 406) */
Value 
    :   PredefinedValue 
    |   ReferencedValue
/* REF(RULE 407) */
PredefinedValue 
    :   Bstring 
    |   BooleanValue 
    |   CharStringValue 
    |   Number /* IntegerValue */
    |   Ostring 
    |   Hstring 
    |   VerdictTypeValue 
    |   Identifier /* EnumeratedValue */
    |   FloatValue 
    |   AddressValue 
    |   OmitKeyword

/* REF(RULE 410) */
CharStringValue 
    :   Cstring 
    |   Quadruple

/* REF(RULE 411) */
Quadruple 
    :   CharKeyword '(' Number ',' Number ',' Number ',' Number ')'

/* REF(RULE 413) */
FloatValue 
    :   FloatDotNotation 
    |   FloatENotation 
    |   NaNKeyword

/* REF(RULE 418) ReferencedValue ::= ExtendedIdentifier [ExtendedFieldReference] */ 
ReferencedValue 
    :   ExtendedIdentifier ExtendedFieldReference
    |   ExtendedIdentifier 

/* REF(RULE 504) */ 
ConstantExpression 
    :   SingleExpression 
    /* TODO */
    /*| CompoundConstExpression*/ 

/* REF(RULE 512) TODO FIXME hack */ 
SingleExpression :
    Value

/* REF(RULE 527) 
    ExtendedFieldReference ::= {
        (Dot Identifier) | ArrayOrBitRef | ('[' Minus ']')
    }+ 
*/
ExtendedFieldReference 
    :   ExtendedFieldReferenceItem
    |   ExtendedFieldReference ExtendedFieldReferenceItem
    
ExtendedFieldReferenceItem 
    :   Dot Identifier
    |   ArrayOrBitRef 
    |   '[' Minus ']'

/* REF(RULE 557) ExtendedIdentifier ::= [Identifier Dot] Identifier */
ExtendedIdentifier 
    :   Identifier Dot Identifier
    |   Identifier

%%

namespace Ttcn3BisonParser {
    void parser::error (
        const location_type& loc, 
        const std::string& msg) {
        std::clog << " error: " << msg << '(' << loc << ')' << std::endl;
    }
}

int main() {
    Ttcn3BisonParser::parser p;
    p.set_debug_level(1);
    return p.parse();
}
