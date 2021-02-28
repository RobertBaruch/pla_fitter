# Generated from rtlil.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from rtlil import *

curr_module = None


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\u0174\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\5\2\65\n\2\3\2\3\2\3\2\7\2:\n\2\f\2\16\2")
        buf.write("=\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\7\5]\n\5\f\5\16\5`\13\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6h\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\7\7r\n\7\f\7\16\7u\13\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u008e\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a4")
        buf.write("\n\n\3\n\3\n\3\n\3\n\3\n\5\n\u00ab\n\n\3\n\3\n\7\n\u00af")
        buf.write("\n\n\f\n\16\n\u00b2\13\n\3\13\3\13\3\13\3\13\7\13\u00b8")
        buf.write("\n\13\f\13\16\13\u00bb\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\7\f\u00c4\n\f\f\f\16\f\u00c7\13\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\5\r\u00ce\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00db\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\7\16\u00e5\n\16\f\16\16\16\u00e8\13\16\3\16\3\16")
        buf.write("\3\16\5\16\u00ed\n\16\3\16\3\16\3\16\7\16\u00f2\n\16\f")
        buf.write("\16\16\16\u00f5\13\16\3\16\3\16\3\16\7\16\u00fa\n\16\f")
        buf.write("\16\16\16\u00fd\13\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\7\17\u010a\n\17\f\17\16\17\u010d")
        buf.write("\13\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u011d\n\20\f\20\16\20\u0120")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0129\n")
        buf.write("\21\f\21\16\21\u012c\13\21\5\21\u012e\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u0135\n\22\f\22\16\22\u0138\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u014c\n\23\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u0160\n\27\f")
        buf.write("\27\16\27\u0163\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0172\n\31\3\31")
        buf.write("\2\3\22\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\2\4\4\2\16\16\26\26\3\2\37#\2\u0182\2\62\3\2")
        buf.write("\2\2\4@\3\2\2\2\6D\3\2\2\2\b^\3\2\2\2\na\3\2\2\2\fk\3")
        buf.write("\2\2\2\16\u008d\3\2\2\2\20\u008f\3\2\2\2\22\u00a3\3\2")
        buf.write("\2\2\24\u00b3\3\2\2\2\26\u00bc\3\2\2\2\30\u00da\3\2\2")
        buf.write("\2\32\u00dc\3\2\2\2\34\u0101\3\2\2\2\36\u0111\3\2\2\2")
        buf.write(" \u0121\3\2\2\2\"\u012f\3\2\2\2$\u014b\3\2\2\2&\u014d")
        buf.write("\3\2\2\2(\u014f\3\2\2\2*\u0155\3\2\2\2,\u015b\3\2\2\2")
        buf.write(".\u0164\3\2\2\2\60\u0171\3\2\2\2\62\64\b\2\1\2\63\65\5")
        buf.write("\4\3\2\64\63\3\2\2\2\64\65\3\2\2\2\65;\3\2\2\2\66\67\5")
        buf.write("\6\4\2\678\b\2\1\28:\3\2\2\29\66\3\2\2\2:=\3\2\2\2;9\3")
        buf.write("\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7\2\2\3?\3\3\2")
        buf.write("\2\2@A\7\3\2\2AB\7*\2\2BC\7+\2\2C\5\3\2\2\2DE\b\4\1\2")
        buf.write("EF\5,\27\2FG\7\4\2\2GH\7(\2\2HI\7+\2\2IJ\b\4\1\2JK\b\4")
        buf.write("\1\2KL\5\b\5\2LM\7\5\2\2MN\7+\2\2N\7\3\2\2\2O]\5\n\6\2")
        buf.write("PQ\5\f\7\2QR\b\5\1\2R]\3\2\2\2ST\5\20\t\2TU\b\5\1\2U]")
        buf.write("\3\2\2\2VW\5\26\f\2WX\b\5\1\2X]\3\2\2\2YZ\5\32\16\2Z[")
        buf.write("\b\5\1\2[]\3\2\2\2\\O\3\2\2\2\\P\3\2\2\2\\S\3\2\2\2\\")
        buf.write("V\3\2\2\2\\Y\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\t")
        buf.write("\3\2\2\2`^\3\2\2\2ab\7\6\2\2bc\7(\2\2cg\b\6\1\2de\5\60")
        buf.write("\31\2ef\b\6\1\2fh\3\2\2\2gd\3\2\2\2gh\3\2\2\2hi\3\2\2")
        buf.write("\2ij\7+\2\2j\13\3\2\2\2kl\b\7\1\2lm\5,\27\2ms\7\7\2\2")
        buf.write("no\5\16\b\2op\b\7\1\2pr\3\2\2\2qn\3\2\2\2ru\3\2\2\2sq")
        buf.write("\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7(\2\2wx\7+\2")
        buf.write("\2xy\b\7\1\2y\r\3\2\2\2z{\7\b\2\2{|\7*\2\2|\u008e\b\b")
        buf.write("\1\2}~\7\t\2\2~\177\7*\2\2\177\u008e\b\b\1\2\u0080\u0081")
        buf.write("\7\n\2\2\u0081\u0082\7*\2\2\u0082\u008e\b\b\1\2\u0083")
        buf.write("\u0084\7\13\2\2\u0084\u0085\7*\2\2\u0085\u008e\b\b\1\2")
        buf.write("\u0086\u0087\7\f\2\2\u0087\u0088\7*\2\2\u0088\u008e\b")
        buf.write("\b\1\2\u0089\u008a\7\r\2\2\u008a\u008e\b\b\1\2\u008b\u008c")
        buf.write("\7\16\2\2\u008c\u008e\b\b\1\2\u008dz\3\2\2\2\u008d}\3")
        buf.write("\2\2\2\u008d\u0080\3\2\2\2\u008d\u0083\3\2\2\2\u008d\u0086")
        buf.write("\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008b\3\2\2\2\u008e")
        buf.write("\17\3\2\2\2\u008f\u0090\7\17\2\2\u0090\u0091\5\22\n\2")
        buf.write("\u0091\u0092\5\22\n\2\u0092\u0093\7+\2\2\u0093\u0094\b")
        buf.write("\t\1\2\u0094\21\3\2\2\2\u0095\u0096\b\n\1\2\u0096\u0097")
        buf.write("\5\60\31\2\u0097\u0098\b\n\1\2\u0098\u00a4\3\2\2\2\u0099")
        buf.write("\u009a\7(\2\2\u009a\u009b\b\n\1\2\u009b\u009c\b\n\1\2")
        buf.write("\u009c\u009d\b\n\1\2\u009d\u00a4\b\n\1\2\u009e\u009f\7")
        buf.write("\23\2\2\u009f\u00a0\5\24\13\2\u00a0\u00a1\7\24\2\2\u00a1")
        buf.write("\u00a2\b\n\1\2\u00a2\u00a4\3\2\2\2\u00a3\u0095\3\2\2\2")
        buf.write("\u00a3\u0099\3\2\2\2\u00a3\u009e\3\2\2\2\u00a4\u00b0\3")
        buf.write("\2\2\2\u00a5\u00a6\f\4\2\2\u00a6\u00a7\7\20\2\2\u00a7")
        buf.write("\u00aa\7*\2\2\u00a8\u00a9\7\21\2\2\u00a9\u00ab\7*\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3")
        buf.write("\2\2\2\u00ac\u00ad\7\22\2\2\u00ad\u00af\b\n\1\2\u00ae")
        buf.write("\u00a5\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\23\3\2\2\2\u00b2\u00b0\3\2")
        buf.write("\2\2\u00b3\u00b9\b\13\1\2\u00b4\u00b5\5\22\n\2\u00b5\u00b6")
        buf.write("\b\13\1\2\u00b6\u00b8\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b8")
        buf.write("\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\25\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\5,\27")
        buf.write("\2\u00bd\u00be\7\25\2\2\u00be\u00bf\7(\2\2\u00bf\u00c0")
        buf.write("\7(\2\2\u00c0\u00c1\7+\2\2\u00c1\u00c5\b\f\1\2\u00c2\u00c4")
        buf.write("\5\30\r\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7\5\2\2\u00c9\u00ca\7")
        buf.write("+\2\2\u00ca\27\3\2\2\2\u00cb\u00cd\7\6\2\2\u00cc\u00ce")
        buf.write("\t\2\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d0\7(\2\2\u00d0\u00d1\5\60\31")
        buf.write("\2\u00d1\u00d2\7+\2\2\u00d2\u00d3\b\r\1\2\u00d3\u00db")
        buf.write("\3\2\2\2\u00d4\u00d5\7\17\2\2\u00d5\u00d6\7(\2\2\u00d6")
        buf.write("\u00d7\5\22\n\2\u00d7\u00d8\7+\2\2\u00d8\u00d9\b\r\1\2")
        buf.write("\u00d9\u00db\3\2\2\2\u00da\u00cb\3\2\2\2\u00da\u00d4\3")
        buf.write("\2\2\2\u00db\31\3\2\2\2\u00dc\u00dd\5,\27\2\u00dd\u00de")
        buf.write("\7\27\2\2\u00de\u00df\7(\2\2\u00df\u00e0\7+\2\2\u00e0")
        buf.write("\u00e6\b\16\1\2\u00e1\u00e2\5*\26\2\u00e2\u00e3\b\16\1")
        buf.write("\2\u00e3\u00e5\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00ec\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\5\34\17")
        buf.write("\2\u00ea\u00eb\b\16\1\2\u00eb\u00ed\3\2\2\2\u00ec\u00e9")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f3\3\2\2\2\u00ee")
        buf.write("\u00ef\5*\26\2\u00ef\u00f0\b\16\1\2\u00f0\u00f2\3\2\2")
        buf.write("\2\u00f1\u00ee\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00fb\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00f7\5\"\22\2\u00f7\u00f8\b\16\1")
        buf.write("\2\u00f8\u00fa\3\2\2\2\u00f9\u00f6\3\2\2\2\u00fa\u00fd")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7\5\2\2")
        buf.write("\u00ff\u0100\7+\2\2\u0100\33\3\2\2\2\u0101\u0102\5,\27")
        buf.write("\2\u0102\u0103\7\30\2\2\u0103\u0104\5\22\n\2\u0104\u0105")
        buf.write("\7+\2\2\u0105\u010b\b\17\1\2\u0106\u0107\5\36\20\2\u0107")
        buf.write("\u0108\b\17\1\2\u0108\u010a\3\2\2\2\u0109\u0106\3\2\2")
        buf.write("\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e")
        buf.write("\u010f\7\5\2\2\u010f\u0110\7+\2\2\u0110\35\3\2\2\2\u0111")
        buf.write("\u0112\5,\27\2\u0112\u0113\7\31\2\2\u0113\u0114\5 \21")
        buf.write("\2\u0114\u0115\7+\2\2\u0115\u011e\b\20\1\2\u0116\u0117")
        buf.write("\5\34\17\2\u0117\u0118\b\20\1\2\u0118\u011d\3\2\2\2\u0119")
        buf.write("\u011a\5*\26\2\u011a\u011b\b\20\1\2\u011b\u011d\3\2\2")
        buf.write("\2\u011c\u0116\3\2\2\2\u011c\u0119\3\2\2\2\u011d\u0120")
        buf.write("\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f")
        buf.write("\37\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u012d\b\21\1\2\u0122")
        buf.write("\u0123\5\22\n\2\u0123\u012a\b\21\1\2\u0124\u0125\7\32")
        buf.write("\2\2\u0125\u0126\5\22\n\2\u0126\u0127\b\21\1\2\u0127\u0129")
        buf.write("\3\2\2\2\u0128\u0124\3\2\2\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012e\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012d\u0122\3\2\2\2\u012d\u012e\3")
        buf.write("\2\2\2\u012e!\3\2\2\2\u012f\u0130\5$\23\2\u0130\u0136")
        buf.write("\b\22\1\2\u0131\u0132\5(\25\2\u0132\u0133\b\22\1\2\u0133")
        buf.write("\u0135\3\2\2\2\u0134\u0131\3\2\2\2\u0135\u0138\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137#\3\2\2")
        buf.write("\2\u0138\u0136\3\2\2\2\u0139\u013a\7\33\2\2\u013a\u013b")
        buf.write("\5&\24\2\u013b\u013c\5\22\n\2\u013c\u013d\7+\2\2\u013d")
        buf.write("\u013e\b\23\1\2\u013e\u014c\3\2\2\2\u013f\u0140\7\33\2")
        buf.write("\2\u0140\u0141\7\34\2\2\u0141\u0142\7+\2\2\u0142\u014c")
        buf.write("\b\23\1\2\u0143\u0144\7\33\2\2\u0144\u0145\7\35\2\2\u0145")
        buf.write("\u0146\7+\2\2\u0146\u014c\b\23\1\2\u0147\u0148\7\33\2")
        buf.write("\2\u0148\u0149\7\36\2\2\u0149\u014a\7+\2\2\u014a\u014c")
        buf.write("\b\23\1\2\u014b\u0139\3\2\2\2\u014b\u013f\3\2\2\2\u014b")
        buf.write("\u0143\3\2\2\2\u014b\u0147\3\2\2\2\u014c%\3\2\2\2\u014d")
        buf.write("\u014e\t\3\2\2\u014e\'\3\2\2\2\u014f\u0150\7$\2\2\u0150")
        buf.write("\u0151\5\22\n\2\u0151\u0152\5\22\n\2\u0152\u0153\7+\2")
        buf.write("\2\u0153\u0154\b\25\1\2\u0154)\3\2\2\2\u0155\u0156\7%")
        buf.write("\2\2\u0156\u0157\5\22\n\2\u0157\u0158\5\22\n\2\u0158\u0159")
        buf.write("\7+\2\2\u0159\u015a\b\26\1\2\u015a+\3\2\2\2\u015b\u0161")
        buf.write("\b\27\1\2\u015c\u015d\5.\30\2\u015d\u015e\b\27\1\2\u015e")
        buf.write("\u0160\3\2\2\2\u015f\u015c\3\2\2\2\u0160\u0163\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162-\3\2\2")
        buf.write("\2\u0163\u0161\3\2\2\2\u0164\u0165\7&\2\2\u0165\u0166")
        buf.write("\7(\2\2\u0166\u0167\b\30\1\2\u0167\u0168\5\60\31\2\u0168")
        buf.write("\u0169\b\30\1\2\u0169\u016a\7+\2\2\u016a/\3\2\2\2\u016b")
        buf.write("\u016c\7)\2\2\u016c\u0172\b\31\1\2\u016d\u016e\7*\2\2")
        buf.write("\u016e\u0172\b\31\1\2\u016f\u0170\7\'\2\2\u0170\u0172")
        buf.write("\b\31\1\2\u0171\u016b\3\2\2\2\u0171\u016d\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0172\61\3\2\2\2\35\64;\\^gs\u008d\u00a3")
        buf.write("\u00aa\u00b0\u00b9\u00c5\u00cd\u00da\u00e6\u00ec\u00f3")
        buf.write("\u00fb\u010b\u011c\u011e\u012a\u012d\u0136\u014b\u0161")
        buf.write("\u0171")
        return buf.getvalue()


class rtlilParser ( Parser ):

    grammarFileName = "rtlil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'autoidx'", "'module'", "'end'", "'parameter'", 
                     "'wire'", "'width'", "'offset'", "'input'", "'output'", 
                     "'inout'", "'upto'", "'signed'", "'connect'", "'['", 
                     "':'", "']'", "'{'", "'}'", "'cell'", "'real'", "'process'", 
                     "'switch'", "'case'", "','", "'sync'", "'global'", 
                     "'init'", "'always'", "'low'", "'high'", "'posedge'", 
                     "'negedge'", "'edge'", "'update'", "'assign'", "'attribute'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "ID", "VALUE", "INT", "EOL", 
                      "SKIP_" ]

    RULE_file_ = 0
    RULE_autoidx_stmt = 1
    RULE_module = 2
    RULE_module_body = 3
    RULE_param_stmt = 4
    RULE_wire = 5
    RULE_wire_option = 6
    RULE_conn_stmt = 7
    RULE_sig_spec = 8
    RULE_sig_specs = 9
    RULE_cell = 10
    RULE_cell_body_stmt = 11
    RULE_process = 12
    RULE_switch = 13
    RULE_case = 14
    RULE_compare = 15
    RULE_sync = 16
    RULE_sync_stmt = 17
    RULE_sync_type = 18
    RULE_update_stmt = 19
    RULE_assign_stmt = 20
    RULE_attr_stmts = 21
    RULE_attr_stmt = 22
    RULE_const = 23

    ruleNames =  [ "file_", "autoidx_stmt", "module", "module_body", "param_stmt", 
                   "wire", "wire_option", "conn_stmt", "sig_spec", "sig_specs", 
                   "cell", "cell_body_stmt", "process", "switch", "case", 
                   "compare", "sync", "sync_stmt", "sync_type", "update_stmt", 
                   "assign_stmt", "attr_stmts", "attr_stmt", "const" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    STRING=37
    ID=38
    VALUE=39
    INT=40
    EOL=41
    SKIP_=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ms = None
            self._module = None # ModuleContext

        def EOF(self):
            return self.getToken(rtlilParser.EOF, 0)

        def autoidx_stmt(self):
            return self.getTypedRuleContext(rtlilParser.Autoidx_stmtContext,0)


        def module(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.ModuleContext)
            else:
                return self.getTypedRuleContext(rtlilParser.ModuleContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_file_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_" ):
                listener.enterFile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_" ):
                listener.exitFile_(self)




    def file_(self):

        localctx = rtlilParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.ms = []
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==rtlilParser.T__0:
                self.state = 49
                self.autoidx_stmt()


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__1 or _la==rtlilParser.T__35:
                self.state = 52
                localctx._module = self.module()
                localctx.ms.append(localctx._module.m)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(rtlilParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Autoidx_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(rtlilParser.INT, 0)

        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def getRuleIndex(self):
            return rtlilParser.RULE_autoidx_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutoidx_stmt" ):
                listener.enterAutoidx_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutoidx_stmt" ):
                listener.exitAutoidx_stmt(self)




    def autoidx_stmt(self):

        localctx = rtlilParser.Autoidx_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_autoidx_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(rtlilParser.T__0)
            self.state = 63
            self.match(rtlilParser.INT)
            self.state = 64
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.m = None
            self._attr_stmts = None # Attr_stmtsContext
            self._ID = None # Token

        def attr_stmts(self):
            return self.getTypedRuleContext(rtlilParser.Attr_stmtsContext,0)


        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(rtlilParser.EOL)
            else:
                return self.getToken(rtlilParser.EOL, i)

        def module_body(self):
            return self.getTypedRuleContext(rtlilParser.Module_bodyContext,0)


        def getRuleIndex(self):
            return rtlilParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = rtlilParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_module)
        try:
            self.enterOuterAlt(localctx, 1)
            global curr_module
            self.state = 67
            localctx._attr_stmts = self.attr_stmts()
            self.state = 68
            self.match(rtlilParser.T__1)
            self.state = 69
            localctx._ID = self.match(rtlilParser.ID)
            self.state = 70
            self.match(rtlilParser.EOL)
            localctx.m = Module((None if localctx._ID is None else localctx._ID.text), localctx._attr_stmts.a)
            curr_module = localctx.m
            self.state = 73
            self.module_body(localctx.m)
            self.state = 74
            self.match(rtlilParser.T__2)
            self.state = 75
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, m=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.m = None
            self._wire = None # WireContext
            self._conn_stmt = None # Conn_stmtContext
            self._cell = None # CellContext
            self._process = None # ProcessContext
            self.m = m

        def param_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Param_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Param_stmtContext,i)


        def wire(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.WireContext)
            else:
                return self.getTypedRuleContext(rtlilParser.WireContext,i)


        def conn_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Conn_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Conn_stmtContext,i)


        def cell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.CellContext)
            else:
                return self.getTypedRuleContext(rtlilParser.CellContext,i)


        def process(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.ProcessContext)
            else:
                return self.getTypedRuleContext(rtlilParser.ProcessContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_module_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_body" ):
                listener.enterModule_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_body" ):
                listener.exitModule_body(self)




    def module_body(self, m):

        localctx = rtlilParser.Module_bodyContext(self, self._ctx, self.state, m)
        self.enterRule(localctx, 6, self.RULE_module_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << rtlilParser.T__3) | (1 << rtlilParser.T__4) | (1 << rtlilParser.T__12) | (1 << rtlilParser.T__18) | (1 << rtlilParser.T__20) | (1 << rtlilParser.T__35))) != 0):
                self.state = 90
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 77
                    self.param_stmt(localctx.m)
                    pass

                elif la_ == 2:
                    self.state = 78
                    localctx._wire = self.wire()
                    localctx.m.add_wire(localctx._wire.w)
                    pass

                elif la_ == 3:
                    self.state = 81
                    localctx._conn_stmt = self.conn_stmt()
                    localctx.m.add_connection(localctx._conn_stmt.c)
                    pass

                elif la_ == 4:
                    self.state = 84
                    localctx._cell = self.cell()
                    localctx.m.add_cell(localctx._cell.c)
                    pass

                elif la_ == 5:
                    self.state = 87
                    localctx._process = self.process()
                    localctx.m.add_process(localctx._process.p)
                    pass


                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, m=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.m = None
            self._ID = None # Token
            self._const = None # ConstContext
            self.m = m

        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def const(self):
            return self.getTypedRuleContext(rtlilParser.ConstContext,0)


        def getRuleIndex(self):
            return rtlilParser.RULE_param_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_stmt" ):
                listener.enterParam_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_stmt" ):
                listener.exitParam_stmt(self)




    def param_stmt(self, m):

        localctx = rtlilParser.Param_stmtContext(self, self._ctx, self.state, m)
        self.enterRule(localctx, 8, self.RULE_param_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(rtlilParser.T__3)
            self.state = 96
            localctx._ID = self.match(rtlilParser.ID)
            localctx.m.add_param((None if localctx._ID is None else localctx._ID.text))
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << rtlilParser.STRING) | (1 << rtlilParser.VALUE) | (1 << rtlilParser.INT))) != 0):
                self.state = 98
                localctx._const = self.const()
                localctx.m.set_param_val((None if localctx._ID is None else localctx._ID.text), localctx._const.c)


            self.state = 103
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WireContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.w = None
            self.opts = None
            self._attr_stmts = None # Attr_stmtsContext
            self._wire_option = None # Wire_optionContext
            self._ID = None # Token

        def attr_stmts(self):
            return self.getTypedRuleContext(rtlilParser.Attr_stmtsContext,0)


        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def wire_option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Wire_optionContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Wire_optionContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_wire

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWire" ):
                listener.enterWire(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWire" ):
                listener.exitWire(self)




    def wire(self):

        localctx = rtlilParser.WireContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_wire)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.opts = {}
            self.state = 106
            localctx._attr_stmts = self.attr_stmts()
            self.state = 107
            self.match(rtlilParser.T__4)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << rtlilParser.T__5) | (1 << rtlilParser.T__6) | (1 << rtlilParser.T__7) | (1 << rtlilParser.T__8) | (1 << rtlilParser.T__9) | (1 << rtlilParser.T__10) | (1 << rtlilParser.T__11))) != 0):
                self.state = 108
                localctx._wire_option = self.wire_option()
                localctx.opts = {**localctx.opts, **localctx._wire_option.o}
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            localctx._ID = self.match(rtlilParser.ID)
            self.state = 117
            self.match(rtlilParser.EOL)
            localctx.w = Wire((None if localctx._ID is None else localctx._ID.text), localctx._attr_stmts.a, localctx.opts)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wire_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.o = None
            self._INT = None # Token

        def INT(self):
            return self.getToken(rtlilParser.INT, 0)

        def getRuleIndex(self):
            return rtlilParser.RULE_wire_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWire_option" ):
                listener.enterWire_option(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWire_option" ):
                listener.exitWire_option(self)




    def wire_option(self):

        localctx = rtlilParser.Wire_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_wire_option)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [rtlilParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(rtlilParser.T__5)
                self.state = 121
                localctx._INT = self.match(rtlilParser.INT)
                localctx.o = {"width": int((None if localctx._INT is None else localctx._INT.text))}
                pass
            elif token in [rtlilParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(rtlilParser.T__6)
                self.state = 124
                localctx._INT = self.match(rtlilParser.INT)
                localctx.o = {"offset": int((None if localctx._INT is None else localctx._INT.text))}
                pass
            elif token in [rtlilParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(rtlilParser.T__7)
                self.state = 127
                localctx._INT = self.match(rtlilParser.INT)
                localctx.o = {"input": int((None if localctx._INT is None else localctx._INT.text))}
                pass
            elif token in [rtlilParser.T__8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.match(rtlilParser.T__8)
                self.state = 130
                localctx._INT = self.match(rtlilParser.INT)
                localctx.o = {"output": int((None if localctx._INT is None else localctx._INT.text))}
                pass
            elif token in [rtlilParser.T__9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.match(rtlilParser.T__9)
                self.state = 133
                localctx._INT = self.match(rtlilParser.INT)
                localctx.o = {"inout": int((None if localctx._INT is None else localctx._INT.text))}
                pass
            elif token in [rtlilParser.T__10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.match(rtlilParser.T__10)
                localctx.o = {"upto": 1}
                pass
            elif token in [rtlilParser.T__11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.match(rtlilParser.T__11)
                localctx.o = {"signed": 1}
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conn_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self.p = None # Sig_specContext
            self.w = None # Sig_specContext

        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def sig_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Sig_specContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Sig_specContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_conn_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConn_stmt" ):
                listener.enterConn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConn_stmt" ):
                listener.exitConn_stmt(self)




    def conn_stmt(self):

        localctx = rtlilParser.Conn_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conn_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(rtlilParser.T__12)
            self.state = 142
            localctx.p = self.sig_spec(0)
            self.state = 143
            localctx.w = self.sig_spec(0)
            self.state = 144
            self.match(rtlilParser.EOL)
            localctx.c = Connection(localctx.p.s, localctx.w.s) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sig_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.sig = None # Sig_specContext
            self._const = None # ConstContext
            self._ID = None # Token
            self._sig_specs = None # Sig_specsContext
            self.st = None # Token
            self.end = None # Token

        def const(self):
            return self.getTypedRuleContext(rtlilParser.ConstContext,0)


        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def sig_specs(self):
            return self.getTypedRuleContext(rtlilParser.Sig_specsContext,0)


        def sig_spec(self):
            return self.getTypedRuleContext(rtlilParser.Sig_specContext,0)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(rtlilParser.INT)
            else:
                return self.getToken(rtlilParser.INT, i)

        def getRuleIndex(self):
            return rtlilParser.RULE_sig_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSig_spec" ):
                listener.enterSig_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSig_spec" ):
                listener.exitSig_spec(self)



    def sig_spec(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = rtlilParser.Sig_specContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_sig_spec, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [rtlilParser.STRING, rtlilParser.VALUE, rtlilParser.INT]:
                self.state = 148
                localctx._const = self.const()
                localctx.s = ConstSigSpec(localctx._const.c) 
                pass
            elif token in [rtlilParser.ID]:
                self.state = 151
                localctx._ID = self.match(rtlilParser.ID)
                assert curr_module is not None
                if (None if localctx._ID is None else localctx._ID.text) not in curr_module.wires:
                  raise SystemError(f"Sigspec refers to wire '{(None if localctx._ID is None else localctx._ID.text)}' that is not present in its module") 
                localctx.s = WireSigSpec(curr_module.wires[(None if localctx._ID is None else localctx._ID.text)]) 
                pass
            elif token in [rtlilParser.T__16]:
                self.state = 156
                self.match(rtlilParser.T__16)
                self.state = 157
                localctx._sig_specs = self.sig_specs()
                self.state = 158
                self.match(rtlilParser.T__17)
                localctx.s = ConcatSigSpec(localctx._sig_specs.ss) 
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = rtlilParser.Sig_specContext(self, _parentctx, _parentState)
                    localctx.sig = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_sig_spec)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    self.match(rtlilParser.T__13)
                    self.state = 165
                    localctx.st = self.match(rtlilParser.INT)
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==rtlilParser.T__14:
                        self.state = 166
                        self.match(rtlilParser.T__14)
                        self.state = 167
                        localctx.end = self.match(rtlilParser.INT)


                    self.state = 170
                    self.match(rtlilParser.T__15)
                    localctx.s = SliceSigSpec(localctx.sig.s, (None if localctx.st is None else localctx.st.text), (None if localctx.end is None else localctx.end.text))  
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Sig_specsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ss = None
            self._sig_spec = None # Sig_specContext

        def sig_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Sig_specContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Sig_specContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_sig_specs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSig_specs" ):
                listener.enterSig_specs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSig_specs" ):
                listener.exitSig_specs(self)




    def sig_specs(self):

        localctx = rtlilParser.Sig_specsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sig_specs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.ss = []
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << rtlilParser.T__16) | (1 << rtlilParser.STRING) | (1 << rtlilParser.ID) | (1 << rtlilParser.VALUE) | (1 << rtlilParser.INT))) != 0):
                self.state = 178
                localctx._sig_spec = self.sig_spec(0)
                localctx.ss.append(localctx._sig_spec.s)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._attr_stmts = None # Attr_stmtsContext
            self.name = None # Token
            self.typ = None # Token

        def attr_stmts(self):
            return self.getTypedRuleContext(rtlilParser.Attr_stmtsContext,0)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(rtlilParser.EOL)
            else:
                return self.getToken(rtlilParser.EOL, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(rtlilParser.ID)
            else:
                return self.getToken(rtlilParser.ID, i)

        def cell_body_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Cell_body_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Cell_body_stmtContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_cell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCell" ):
                listener.enterCell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCell" ):
                listener.exitCell(self)




    def cell(self):

        localctx = rtlilParser.CellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            localctx._attr_stmts = self.attr_stmts()
            self.state = 187
            self.match(rtlilParser.T__18)
            self.state = 188
            localctx.name = self.match(rtlilParser.ID)
            self.state = 189
            localctx.typ = self.match(rtlilParser.ID)
            self.state = 190
            self.match(rtlilParser.EOL)
            localctx.c = Cell((None if localctx.name is None else localctx.name.text), (None if localctx.typ is None else localctx.typ.text), localctx._attr_stmts.a)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__3 or _la==rtlilParser.T__12:
                self.state = 192
                self.cell_body_stmt(localctx.c)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self.match(rtlilParser.T__2)
            self.state = 199
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cell_body_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, c=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._ID = None # Token
            self._const = None # ConstContext
            self._sig_spec = None # Sig_specContext
            self.c = c

        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def const(self):
            return self.getTypedRuleContext(rtlilParser.ConstContext,0)


        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def sig_spec(self):
            return self.getTypedRuleContext(rtlilParser.Sig_specContext,0)


        def getRuleIndex(self):
            return rtlilParser.RULE_cell_body_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCell_body_stmt" ):
                listener.enterCell_body_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCell_body_stmt" ):
                listener.exitCell_body_stmt(self)




    def cell_body_stmt(self, c):

        localctx = rtlilParser.Cell_body_stmtContext(self, self._ctx, self.state, c)
        self.enterRule(localctx, 22, self.RULE_cell_body_stmt)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [rtlilParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(rtlilParser.T__3)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==rtlilParser.T__11 or _la==rtlilParser.T__19:
                    self.state = 202
                    _la = self._input.LA(1)
                    if not(_la==rtlilParser.T__11 or _la==rtlilParser.T__19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 205
                localctx._ID = self.match(rtlilParser.ID)
                self.state = 206
                localctx._const = self.const()
                self.state = 207
                self.match(rtlilParser.EOL)
                localctx.c.add_param((None if localctx._ID is None else localctx._ID.text), localctx._const.c)
                pass
            elif token in [rtlilParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(rtlilParser.T__12)
                self.state = 211
                localctx._ID = self.match(rtlilParser.ID)
                self.state = 212
                localctx._sig_spec = self.sig_spec(0)
                self.state = 213
                self.match(rtlilParser.EOL)
                localctx.c.set_port((None if localctx._ID is None else localctx._ID.text), localctx._sig_spec.s)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.p = None
            self._attr_stmts = None # Attr_stmtsContext
            self._ID = None # Token
            self.a1 = None # Assign_stmtContext
            self._switch = None # SwitchContext
            self.a2 = None # Assign_stmtContext
            self._sync = None # SyncContext

        def attr_stmts(self):
            return self.getTypedRuleContext(rtlilParser.Attr_stmtsContext,0)


        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(rtlilParser.EOL)
            else:
                return self.getToken(rtlilParser.EOL, i)

        def switch(self):
            return self.getTypedRuleContext(rtlilParser.SwitchContext,0)


        def sync(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.SyncContext)
            else:
                return self.getTypedRuleContext(rtlilParser.SyncContext,i)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Assign_stmtContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_process

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcess" ):
                listener.enterProcess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcess" ):
                listener.exitProcess(self)




    def process(self):

        localctx = rtlilParser.ProcessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            localctx._attr_stmts = self.attr_stmts()
            self.state = 219
            self.match(rtlilParser.T__20)
            self.state = 220
            localctx._ID = self.match(rtlilParser.ID)
            self.state = 221
            self.match(rtlilParser.EOL)
            localctx.p = Process((None if localctx._ID is None else localctx._ID.text), localctx._attr_stmts.a)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 223
                    localctx.a1 = self.assign_stmt()
                    localctx.p.add_assignment(localctx.a1.s) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==rtlilParser.T__21 or _la==rtlilParser.T__35:
                self.state = 231
                localctx._switch = self.switch()
                localctx.p.set_switch(localctx._switch.s)


            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__34:
                self.state = 236
                localctx.a2 = self.assign_stmt()
                localctx.p.add_assignment(localctx.a2.s)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__24:
                self.state = 244
                localctx._sync = self.sync()
                localctx.p.add_sync(localctx._sync.s)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(rtlilParser.T__2)
            self.state = 253
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._attr_stmts = None # Attr_stmtsContext
            self._sig_spec = None # Sig_specContext
            self._case = None # CaseContext

        def attr_stmts(self):
            return self.getTypedRuleContext(rtlilParser.Attr_stmtsContext,0)


        def sig_spec(self):
            return self.getTypedRuleContext(rtlilParser.Sig_specContext,0)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(rtlilParser.EOL)
            else:
                return self.getToken(rtlilParser.EOL, i)

        def case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.CaseContext)
            else:
                return self.getTypedRuleContext(rtlilParser.CaseContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_switch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch" ):
                listener.enterSwitch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch" ):
                listener.exitSwitch(self)




    def switch(self):

        localctx = rtlilParser.SwitchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_switch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            localctx._attr_stmts = self.attr_stmts()
            self.state = 256
            self.match(rtlilParser.T__21)
            self.state = 257
            localctx._sig_spec = self.sig_spec(0)
            self.state = 258
            self.match(rtlilParser.EOL)
            localctx.s = Switch(localctx._sig_spec.s, localctx._attr_stmts.a)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__22 or _la==rtlilParser.T__35:
                self.state = 260
                localctx._case = self.case()
                localctx.s.add_case(localctx._case.c)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self.match(rtlilParser.T__2)
            self.state = 269
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._attr_stmts = None # Attr_stmtsContext
            self._compare = None # CompareContext
            self._switch = None # SwitchContext
            self._assign_stmt = None # Assign_stmtContext

        def attr_stmts(self):
            return self.getTypedRuleContext(rtlilParser.Attr_stmtsContext,0)


        def compare(self):
            return self.getTypedRuleContext(rtlilParser.CompareContext,0)


        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def switch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.SwitchContext)
            else:
                return self.getTypedRuleContext(rtlilParser.SwitchContext,i)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Assign_stmtContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase" ):
                listener.enterCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase" ):
                listener.exitCase(self)




    def case(self):

        localctx = rtlilParser.CaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            localctx._attr_stmts = self.attr_stmts()
            self.state = 272
            self.match(rtlilParser.T__22)
            self.state = 273
            localctx._compare = self.compare()
            self.state = 274
            self.match(rtlilParser.EOL)
            localctx.c = Case(localctx._compare.ss, localctx._attr_stmts.a)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [rtlilParser.T__21, rtlilParser.T__35]:
                        self.state = 276
                        localctx._switch = self.switch()
                        localctx.c.add_switch(localctx._switch.s)
                        pass
                    elif token in [rtlilParser.T__34]:
                        self.state = 279
                        localctx._assign_stmt = self.assign_stmt()
                        localctx.c.add_assignment(localctx._assign_stmt.s)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ss = None
            self.s1 = None # Sig_specContext
            self.s2 = None # Sig_specContext

        def sig_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Sig_specContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Sig_specContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = rtlilParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.ss = []
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << rtlilParser.T__16) | (1 << rtlilParser.STRING) | (1 << rtlilParser.ID) | (1 << rtlilParser.VALUE) | (1 << rtlilParser.INT))) != 0):
                self.state = 288
                localctx.s1 = self.sig_spec(0)
                localctx.ss.append(localctx.s1.s)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==rtlilParser.T__23:
                    self.state = 290
                    self.match(rtlilParser.T__23)
                    self.state = 291
                    localctx.s2 = self.sig_spec(0)
                    localctx.ss.append(localctx.s2.s)
                    self.state = 298
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SyncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._sync_stmt = None # Sync_stmtContext
            self._update_stmt = None # Update_stmtContext

        def sync_stmt(self):
            return self.getTypedRuleContext(rtlilParser.Sync_stmtContext,0)


        def update_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Update_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Update_stmtContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_sync

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSync" ):
                listener.enterSync(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSync" ):
                listener.exitSync(self)




    def sync(self):

        localctx = rtlilParser.SyncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sync)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            localctx._sync_stmt = self.sync_stmt()
            localctx.s = localctx._sync_stmt.s
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__33:
                self.state = 303
                localctx._update_stmt = self.update_stmt()
                localctx.s.add_update(localctx._update_stmt.s)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sync_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._sync_type = None # Sync_typeContext
            self._sig_spec = None # Sig_specContext

        def sync_type(self):
            return self.getTypedRuleContext(rtlilParser.Sync_typeContext,0)


        def sig_spec(self):
            return self.getTypedRuleContext(rtlilParser.Sig_specContext,0)


        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def getRuleIndex(self):
            return rtlilParser.RULE_sync_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSync_stmt" ):
                listener.enterSync_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSync_stmt" ):
                listener.exitSync_stmt(self)




    def sync_stmt(self):

        localctx = rtlilParser.Sync_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sync_stmt)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(rtlilParser.T__24)
                self.state = 312
                localctx._sync_type = self.sync_type()
                self.state = 313
                localctx._sig_spec = self.sig_spec(0)
                self.state = 314
                self.match(rtlilParser.EOL)
                localctx.s = Sync((None if localctx._sync_type is None else self._input.getText(localctx._sync_type.start,localctx._sync_type.stop)), localctx._sig_spec.s)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(rtlilParser.T__24)
                self.state = 318
                self.match(rtlilParser.T__25)
                self.state = 319
                self.match(rtlilParser.EOL)
                localctx.s = Sync("global")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(rtlilParser.T__24)
                self.state = 322
                self.match(rtlilParser.T__26)
                self.state = 323
                self.match(rtlilParser.EOL)
                localctx.s = Sync("init")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.match(rtlilParser.T__24)
                self.state = 326
                self.match(rtlilParser.T__27)
                self.state = 327
                self.match(rtlilParser.EOL)
                localctx.s = Sync("always")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sync_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rtlilParser.RULE_sync_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSync_type" ):
                listener.enterSync_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSync_type" ):
                listener.exitSync_type(self)




    def sync_type(self):

        localctx = rtlilParser.Sync_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_sync_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << rtlilParser.T__28) | (1 << rtlilParser.T__29) | (1 << rtlilParser.T__30) | (1 << rtlilParser.T__31) | (1 << rtlilParser.T__32))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.dest = None # Sig_specContext
            self.src = None # Sig_specContext

        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def sig_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Sig_specContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Sig_specContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_update_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate_stmt" ):
                listener.enterUpdate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate_stmt" ):
                listener.exitUpdate_stmt(self)




    def update_stmt(self):

        localctx = rtlilParser.Update_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_update_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(rtlilParser.T__33)
            self.state = 334
            localctx.dest = self.sig_spec(0)
            self.state = 335
            localctx.src = self.sig_spec(0)
            self.state = 336
            self.match(rtlilParser.EOL)
            localctx.s = Assignment(localctx.dest.s, localctx.src.s)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.dest = None # Sig_specContext
            self.src = None # Sig_specContext

        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def sig_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Sig_specContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Sig_specContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = rtlilParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(rtlilParser.T__34)
            self.state = 340
            localctx.dest = self.sig_spec(0)
            self.state = 341
            localctx.src = self.sig_spec(0)
            self.state = 342
            self.match(rtlilParser.EOL)
            localctx.s = Assignment(localctx.dest.s, localctx.src.s)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.a = None
            self._attr_stmt = None # Attr_stmtContext

        def attr_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rtlilParser.Attr_stmtContext)
            else:
                return self.getTypedRuleContext(rtlilParser.Attr_stmtContext,i)


        def getRuleIndex(self):
            return rtlilParser.RULE_attr_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_stmts" ):
                listener.enterAttr_stmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_stmts" ):
                listener.exitAttr_stmts(self)




    def attr_stmts(self):

        localctx = rtlilParser.Attr_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_attr_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.a = {}
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==rtlilParser.T__35:
                self.state = 346
                localctx._attr_stmt = self.attr_stmt()
                localctx.a[localctx._attr_stmt.i] = localctx._attr_stmt.c
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.i = None
            self.c = None
            self._ID = None # Token
            self._const = None # ConstContext

        def ID(self):
            return self.getToken(rtlilParser.ID, 0)

        def const(self):
            return self.getTypedRuleContext(rtlilParser.ConstContext,0)


        def EOL(self):
            return self.getToken(rtlilParser.EOL, 0)

        def getRuleIndex(self):
            return rtlilParser.RULE_attr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_stmt" ):
                listener.enterAttr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_stmt" ):
                listener.exitAttr_stmt(self)




    def attr_stmt(self):

        localctx = rtlilParser.Attr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_attr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(rtlilParser.T__35)
            self.state = 355
            localctx._ID = self.match(rtlilParser.ID)
            localctx.i = (None if localctx._ID is None else localctx._ID.text)
            self.state = 357
            localctx._const = self.const()
            localctx.c = localctx._const.c
            self.state = 359
            self.match(rtlilParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._VALUE = None # Token
            self._INT = None # Token
            self._STRING = None # Token

        def VALUE(self):
            return self.getToken(rtlilParser.VALUE, 0)

        def INT(self):
            return self.getToken(rtlilParser.INT, 0)

        def STRING(self):
            return self.getToken(rtlilParser.STRING, 0)

        def getRuleIndex(self):
            return rtlilParser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)




    def const(self):

        localctx = rtlilParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_const)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [rtlilParser.VALUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                localctx._VALUE = self.match(rtlilParser.VALUE)
                localctx.c = ConstValue((None if localctx._VALUE is None else localctx._VALUE.text))
                pass
            elif token in [rtlilParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                localctx._INT = self.match(rtlilParser.INT)
                localctx.c = ConstInt((None if localctx._INT is None else localctx._INT.text))
                pass
            elif token in [rtlilParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                localctx._STRING = self.match(rtlilParser.STRING)
                localctx.c = ConstString((None if localctx._STRING is None else localctx._STRING.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.sig_spec_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sig_spec_sempred(self, localctx:Sig_specContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




