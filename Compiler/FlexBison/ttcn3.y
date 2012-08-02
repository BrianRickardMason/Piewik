

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

%token IDENTIFIER 
%token COMMENT_START COMMENT_END COMMENT_BODY
%token INTEGER_CONSTANT FLOAT_CONSTANT
%token UNDERSCORE

%start module

%%  /* Grammar */

module 
    :	words {
        clog << "Hai" << endl;
    }
    ;

words
	:   /*empty*/{
        clog << "Bai" << endl;
	}
        |   IDENTIFIER words {
        clog << "Word!" << endl;
	}

%%

namespace Ttcn3BisonParser {
    void parser::error (
        const location_type& loc, 
        const std::string& msg) {
        std::clog << " error: " << msg << "(" << loc.begin << "/" << loc.end << ")" << std::endl;
    }
}

int main() {
    Ttcn3BisonParser::parser p;
    
    return p.parse();
}
