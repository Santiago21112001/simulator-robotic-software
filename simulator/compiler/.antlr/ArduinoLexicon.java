// Generated from e:\Asignaturas\Cuarto\TFG\SimuladorSoftwareRobots\simulator\compiler\ArduinoLexicon.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ArduinoLexicon extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, INT_CONST=2, FLOAT_CONST=3, CHAR_CONST=4, STRING_CONST=5, LINE_COMMENT=6, 
		MULTILINE_COMMENT=7, WHITESPACE=8;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ID", "INT_CONST", "FLOAT_CONST", "CHAR_CONST", "STRING_CONST", "LINE_COMMENT", 
			"MULTILINE_COMMENT", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "INT_CONST", "FLOAT_CONST", "CHAR_CONST", "STRING_CONST", 
			"LINE_COMMENT", "MULTILINE_COMMENT", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ArduinoLexicon(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ArduinoLexicon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\nU\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\7\2\26"+
		"\n\2\f\2\16\2\31\13\2\3\3\6\3\34\n\3\r\3\16\3\35\3\4\6\4!\n\4\r\4\16\4"+
		"\"\3\4\3\4\6\4\'\n\4\r\4\16\4(\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7"+
		"\3\7\3\7\7\7\67\n\7\f\7\16\7:\13\7\3\7\5\7=\n\7\3\7\3\7\3\b\3\b\3\b\3"+
		"\b\7\bE\n\b\f\b\16\bH\13\b\3\b\3\b\3\b\3\b\3\b\3\t\6\tP\n\t\r\t\16\tQ"+
		"\3\t\3\t\48F\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\t\5\2C\\aac|\6"+
		"\2\62;C\\aac|\3\2\62;\5\2\f\f))^^\5\2\f\f$$^^\3\3\f\f\5\2\13\f\17\17\""+
		"\"\2[\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r"+
		"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\33\3\2\2\2\7 \3\2\2"+
		"\2\t*\3\2\2\2\13.\3\2\2\2\r\62\3\2\2\2\17@\3\2\2\2\21O\3\2\2\2\23\27\t"+
		"\2\2\2\24\26\t\3\2\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3"+
		"\2\2\2\30\4\3\2\2\2\31\27\3\2\2\2\32\34\t\4\2\2\33\32\3\2\2\2\34\35\3"+
		"\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\6\3\2\2\2\37!\t\4\2\2 \37\3\2\2"+
		"\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#$\3\2\2\2$&\7\60\2\2%\'\t\4\2\2&%"+
		"\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)\b\3\2\2\2*+\7)\2\2+,\n\5\2\2"+
		",-\7)\2\2-\n\3\2\2\2./\7$\2\2/\60\n\6\2\2\60\61\7$\2\2\61\f\3\2\2\2\62"+
		"\63\7\61\2\2\63\64\7\61\2\2\648\3\2\2\2\65\67\13\2\2\2\66\65\3\2\2\2\67"+
		":\3\2\2\289\3\2\2\28\66\3\2\2\29<\3\2\2\2:8\3\2\2\2;=\t\7\2\2<;\3\2\2"+
		"\2=>\3\2\2\2>?\b\7\2\2?\16\3\2\2\2@A\7\61\2\2AB\7,\2\2BF\3\2\2\2CE\13"+
		"\2\2\2DC\3\2\2\2EH\3\2\2\2FG\3\2\2\2FD\3\2\2\2GI\3\2\2\2HF\3\2\2\2IJ\7"+
		",\2\2JK\7\61\2\2KL\3\2\2\2LM\b\b\2\2M\20\3\2\2\2NP\t\b\2\2ON\3\2\2\2P"+
		"Q\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\b\t\2\2T\22\3\2\2\2\13\2\27"+
		"\35\"(8<FQ\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}