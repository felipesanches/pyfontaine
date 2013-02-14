# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'Adobe Latin 4'
    native_name = u''

    def glyphs(self):
        # from http://blogs.adobe.com/typblography/2008/08/extended_latin.html
        glyphs  = [0x0020] # SPACE
        glyphs += [0x0021] # EXCLAMATION MARK
        glyphs += [0x0022] # QUOTATION MARK
        glyphs += [0x0023] # NUMBER SIGN
        glyphs += [0x0024] # DOLLAR SIGN
        glyphs += [0x0025] # PERCENT SIGN
        glyphs += [0x0026] # AMPERSAND
        glyphs += [0x0027] # APOSTROPHE
        glyphs += [0x0028] # LEFT PARENTHESIS
        glyphs += [0x0029] # RIGHT PARENTHESIS
        glyphs += [0x002A] # ASTERISK
        glyphs += [0x002B] # PLUS SIGN
        glyphs += [0x002C] # COMMA
        glyphs += [0x002D] # HYPHEN-MINUS
        glyphs += [0x002E] # FULL STOP
        glyphs += [0x002F] # SOLIDUS
        glyphs += [0x0030] # DIGIT ZERO
        glyphs += [0x0031] # DIGIT ONE
        glyphs += [0x0032] # DIGIT TWO
        glyphs += [0x0033] # DIGIT THREE
        glyphs += [0x0034] # DIGIT FOUR
        glyphs += [0x0035] # DIGIT FIVE
        glyphs += [0x0036] # DIGIT SIX
        glyphs += [0x0037] # DIGIT SEVEN
        glyphs += [0x0038] # DIGIT EIGHT
        glyphs += [0x0039] # DIGIT NINE
        glyphs += [0x003A] # COLON
        glyphs += [0x003B] # SEMICOLON
        glyphs += [0x003C] # LESS-THAN SIGN
        glyphs += [0x003D] # EQUALS SIGN
        glyphs += [0x003E] # GREATER-THAN SIGN
        glyphs += [0x003F] # QUESTION MARK
        glyphs += [0x0040] # COMMERCIAL AT
        glyphs += [0x0041] # LATIN CAPITAL LETTER A
        glyphs += [0x0042] # LATIN CAPITAL LETTER B
        glyphs += [0x0043] # LATIN CAPITAL LETTER C
        glyphs += [0x0044] # LATIN CAPITAL LETTER D
        glyphs += [0x0045] # LATIN CAPITAL LETTER E
        glyphs += [0x0046] # LATIN CAPITAL LETTER F
        glyphs += [0x0047] # LATIN CAPITAL LETTER G
        glyphs += [0x0048] # LATIN CAPITAL LETTER H
        glyphs += [0x0049] # LATIN CAPITAL LETTER I
        glyphs += [0x004A] # LATIN CAPITAL LETTER J
        glyphs += [0x004B] # LATIN CAPITAL LETTER K
        glyphs += [0x004C] # LATIN CAPITAL LETTER L
        glyphs += [0x004D] # LATIN CAPITAL LETTER M
        glyphs += [0x004E] # LATIN CAPITAL LETTER N
        glyphs += [0x004F] # LATIN CAPITAL LETTER O
        glyphs += [0x0050] # LATIN CAPITAL LETTER P
        glyphs += [0x0051] # LATIN CAPITAL LETTER Q
        glyphs += [0x0052] # LATIN CAPITAL LETTER R
        glyphs += [0x0053] # LATIN CAPITAL LETTER S
        glyphs += [0x0054] # LATIN CAPITAL LETTER T
        glyphs += [0x0055] # LATIN CAPITAL LETTER U
        glyphs += [0x0056] # LATIN CAPITAL LETTER V
        glyphs += [0x0057] # LATIN CAPITAL LETTER W
        glyphs += [0x0058] # LATIN CAPITAL LETTER X
        glyphs += [0x0059] # LATIN CAPITAL LETTER Y
        glyphs += [0x005A] # LATIN CAPITAL LETTER Z
        glyphs += [0x005B] # LEFT SQUARE BRACKET
        glyphs += [0x005C] # REVERSE SOLIDUS
        glyphs += [0x005D] # RIGHT SQUARE BRACKET
        glyphs += [0x005E] # CIRCUMFLEX ACCENT
        glyphs += [0x005F] # LOW LINE
        glyphs += [0x0060] # GRAVE ACCENT
        glyphs += [0x0061] # LATIN SMALL LETTER A
        glyphs += [0x0062] # LATIN SMALL LETTER B
        glyphs += [0x0063] # LATIN SMALL LETTER C
        glyphs += [0x0064] # LATIN SMALL LETTER D
        glyphs += [0x0065] # LATIN SMALL LETTER E
        glyphs += [0x0066] # LATIN SMALL LETTER F
        glyphs += [0x0067] # LATIN SMALL LETTER G
        glyphs += [0x0068] # LATIN SMALL LETTER H
        glyphs += [0x0069] # LATIN SMALL LETTER I
        glyphs += [0x006A] # LATIN SMALL LETTER J
        glyphs += [0x006B] # LATIN SMALL LETTER K
        glyphs += [0x006C] # LATIN SMALL LETTER L
        glyphs += [0x006D] # LATIN SMALL LETTER M
        glyphs += [0x006E] # LATIN SMALL LETTER N
        glyphs += [0x006F] # LATIN SMALL LETTER O
        glyphs += [0x0070] # LATIN SMALL LETTER P
        glyphs += [0x0071] # LATIN SMALL LETTER Q
        glyphs += [0x0072] # LATIN SMALL LETTER R
        glyphs += [0x0073] # LATIN SMALL LETTER S
        glyphs += [0x0074] # LATIN SMALL LETTER T
        glyphs += [0x0075] # LATIN SMALL LETTER U
        glyphs += [0x0076] # LATIN SMALL LETTER V
        glyphs += [0x0077] # LATIN SMALL LETTER W
        glyphs += [0x0078] # LATIN SMALL LETTER X
        glyphs += [0x0079] # LATIN SMALL LETTER Y
        glyphs += [0x007A] # LATIN SMALL LETTER Z
        glyphs += [0x007B] # LEFT CURLY BRACKET
        glyphs += [0x007C] # VERTICAL LINE
        glyphs += [0x007D] # RIGHT CURLY BRACKET
        glyphs += [0x007E] # TILDE
        glyphs += [0x00A0] # NO-BREAK SPACE
        glyphs += [0x00A1] # INVERTED EXCLAMATION MARK
        glyphs += [0x00A2] # CENT SIGN
        glyphs += [0x00A3] # POUND SIGN
        glyphs += [0x00A4] # CURRENCY SIGN
        glyphs += [0x00A5] # YEN SIGN
        glyphs += [0x00A6] # BROKEN BAR
        glyphs += [0x00A7] # SECTION SIGN
        glyphs += [0x00A8] # DIAERESIS
        glyphs += [0x00A9] # COPYRIGHT SIGN
        glyphs += [0x00AA] # FEMININE ORDINAL INDICATOR
        glyphs += [0x00AB] # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        glyphs += [0x00AC] # NOT SIGN
        glyphs += [0x00AD] # SOFT HYPHEN
        glyphs += [0x00AE] # REGISTERED SIGN
        glyphs += [0x00AF] # MACRON
        glyphs += [0x00B0] # DEGREE SIGN
        glyphs += [0x00B1] # PLUS-MINUS SIGN
        glyphs += [0x00B2] # SUPERSCRIPT TWO
        glyphs += [0x00B3] # SUPERSCRIPT THREE
        glyphs += [0x00B4] # ACUTE ACCENT
        glyphs += [0x00B5] # MICRO SIGN
        glyphs += [0x00B6] # PILCROW SIGN
        glyphs += [0x00B7] # MIDDLE DOT
        glyphs += [0x00B8] # CEDILLA
        glyphs += [0x00B9] # SUPERSCRIPT ONE
        glyphs += [0x00BA] # MASCULINE ORDINAL INDICATOR
        glyphs += [0x00BB] # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        glyphs += [0x00BC] # VULGAR FRACTION ONE QUARTER
        glyphs += [0x00BD] # VULGAR FRACTION ONE HALF
        glyphs += [0x00BE] # VULGAR FRACTION THREE QUARTERS
        glyphs += [0x00BF] # INVERTED QUESTION MARK
        glyphs += [0x00C0] # LATIN CAPITAL LETTER A WITH GRAVE
        glyphs += [0x00C1] # LATIN CAPITAL LETTER A WITH ACUTE
        glyphs += [0x00C2] # LATIN CAPITAL LETTER A WITH CIRCUMFLEX
        glyphs += [0x00C3] # LATIN CAPITAL LETTER A WITH TILDE
        glyphs += [0x00C4] # LATIN CAPITAL LETTER A WITH DIAERESIS
        glyphs += [0x00C5] # LATIN CAPITAL LETTER A WITH RING ABOVE
        glyphs += [0x00C6] # LATIN CAPITAL LETTER AE
        glyphs += [0x00C7] # LATIN CAPITAL LETTER C WITH CEDILLA
        glyphs += [0x00C8] # LATIN CAPITAL LETTER E WITH GRAVE
        glyphs += [0x00C9] # LATIN CAPITAL LETTER E WITH ACUTE
        glyphs += [0x00CA] # LATIN CAPITAL LETTER E WITH CIRCUMFLEX
        glyphs += [0x00CB] # LATIN CAPITAL LETTER E WITH DIAERESIS
        glyphs += [0x00CC] # LATIN CAPITAL LETTER I WITH GRAVE
        glyphs += [0x00CD] # LATIN CAPITAL LETTER I WITH ACUTE
        glyphs += [0x00CE] # LATIN CAPITAL LETTER I WITH CIRCUMFLEX
        glyphs += [0x00CF] # LATIN CAPITAL LETTER I WITH DIAERESIS
        glyphs += [0x00D0] # LATIN CAPITAL LETTER ETH
        glyphs += [0x00D1] # LATIN CAPITAL LETTER N WITH TILDE
        glyphs += [0x00D2] # LATIN CAPITAL LETTER O WITH GRAVE
        glyphs += [0x00D3] # LATIN CAPITAL LETTER O WITH ACUTE
        glyphs += [0x00D4] # LATIN CAPITAL LETTER O WITH CIRCUMFLEX
        glyphs += [0x00D5] # LATIN CAPITAL LETTER O WITH TILDE
        glyphs += [0x00D6] # LATIN CAPITAL LETTER O WITH DIAERESIS
        glyphs += [0x00D7] # MULTIPLICATION SIGN
        glyphs += [0x00D8] # LATIN CAPITAL LETTER O WITH STROKE
        glyphs += [0x00D9] # LATIN CAPITAL LETTER U WITH GRAVE
        glyphs += [0x00DA] # LATIN CAPITAL LETTER U WITH ACUTE
        glyphs += [0x00DB] # LATIN CAPITAL LETTER U WITH CIRCUMFLEX
        glyphs += [0x00DC] # LATIN CAPITAL LETTER U WITH DIAERESIS
        glyphs += [0x00DD] # LATIN CAPITAL LETTER Y WITH ACUTE
        glyphs += [0x00DE] # LATIN CAPITAL LETTER THORN
        glyphs += [0x00DF] # LATIN SMALL LETTER SHARP S
        glyphs += [0x00E0] # LATIN SMALL LETTER A WITH GRAVE
        glyphs += [0x00E1] # LATIN SMALL LETTER A WITH ACUTE
        glyphs += [0x00E2] # LATIN SMALL LETTER A WITH CIRCUMFLEX
        glyphs += [0x00E3] # LATIN SMALL LETTER A WITH TILDE
        glyphs += [0x00E4] # LATIN SMALL LETTER A WITH DIAERESIS
        glyphs += [0x00E5] # LATIN SMALL LETTER A WITH RING ABOVE
        glyphs += [0x00E6] # LATIN SMALL LETTER AE
        glyphs += [0x00E7] # LATIN SMALL LETTER C WITH CEDILLA
        glyphs += [0x00E8] # LATIN SMALL LETTER E WITH GRAVE
        glyphs += [0x00E9] # LATIN SMALL LETTER E WITH ACUTE
        glyphs += [0x00EA] # LATIN SMALL LETTER E WITH CIRCUMFLEX
        glyphs += [0x00EB] # LATIN SMALL LETTER E WITH DIAERESIS
        glyphs += [0x00EC] # LATIN SMALL LETTER I WITH GRAVE
        glyphs += [0x00ED] # LATIN SMALL LETTER I WITH ACUTE
        glyphs += [0x00EE] # LATIN SMALL LETTER I WITH CIRCUMFLEX
        glyphs += [0x00EF] # LATIN SMALL LETTER I WITH DIAERESIS
        glyphs += [0x00F0] # LATIN SMALL LETTER ETH
        glyphs += [0x00F1] # LATIN SMALL LETTER N WITH TILDE
        glyphs += [0x00F2] # LATIN SMALL LETTER O WITH GRAVE
        glyphs += [0x00F3] # LATIN SMALL LETTER O WITH ACUTE
        glyphs += [0x00F4] # LATIN SMALL LETTER O WITH CIRCUMFLEX
        glyphs += [0x00F5] # LATIN SMALL LETTER O WITH TILDE
        glyphs += [0x00F6] # LATIN SMALL LETTER O WITH DIAERESIS
        glyphs += [0x00F7] # DIVISION SIGN
        glyphs += [0x00F8] # LATIN SMALL LETTER O WITH STROKE
        glyphs += [0x00F9] # LATIN SMALL LETTER U WITH GRAVE
        glyphs += [0x00FA] # LATIN SMALL LETTER U WITH ACUTE
        glyphs += [0x00FB] # LATIN SMALL LETTER U WITH CIRCUMFLEX
        glyphs += [0x00FC] # LATIN SMALL LETTER U WITH DIAERESIS
        glyphs += [0x00FD] # LATIN SMALL LETTER Y WITH ACUTE
        glyphs += [0x00FE] # LATIN SMALL LETTER THORN
        glyphs += [0x00FF] # LATIN SMALL LETTER Y WITH DIAERESIS
        glyphs += [0x0100] # LATIN CAPITAL LETTER A WITH MACRON
        glyphs += [0x0101] # LATIN SMALL LETTER A WITH MACRON
        glyphs += [0x0102] # LATIN CAPITAL LETTER A WITH BREVE
        glyphs += [0x0103] # LATIN SMALL LETTER A WITH BREVE
        glyphs += [0x0104] # LATIN CAPITAL LETTER A WITH OGONEK
        glyphs += [0x0105] # LATIN SMALL LETTER A WITH OGONEK
        glyphs += [0x0106] # LATIN CAPITAL LETTER C WITH ACUTE
        glyphs += [0x0107] # LATIN SMALL LETTER C WITH ACUTE
        glyphs += [0x0108] # LATIN CAPITAL LETTER C WITH CIRCUMFLEX
        glyphs += [0x0109] # LATIN SMALL LETTER C WITH CIRCUMFLEX
        glyphs += [0x010A] # LATIN CAPITAL LETTER C WITH DOT ABOVE
        glyphs += [0x010B] # LATIN SMALL LETTER C WITH DOT ABOVE
        glyphs += [0x010C] # LATIN CAPITAL LETTER C WITH CARON
        glyphs += [0x010D] # LATIN SMALL LETTER C WITH CARON
        glyphs += [0x010E] # LATIN CAPITAL LETTER D WITH CARON
        glyphs += [0x010F] # LATIN SMALL LETTER D WITH CARON
        glyphs += [0x0110] # LATIN CAPITAL LETTER D WITH STROKE
        glyphs += [0x0111] # LATIN SMALL LETTER D WITH STROKE
        glyphs += [0x0112] # LATIN CAPITAL LETTER E WITH MACRON
        glyphs += [0x0113] # LATIN SMALL LETTER E WITH MACRON
        glyphs += [0x0114] # LATIN CAPITAL LETTER E WITH BREVE
        glyphs += [0x0115] # LATIN SMALL LETTER E WITH BREVE
        glyphs += [0x0116] # LATIN CAPITAL LETTER E WITH DOT ABOVE
        glyphs += [0x0117] # LATIN SMALL LETTER E WITH DOT ABOVE
        glyphs += [0x0118] # LATIN CAPITAL LETTER E WITH OGONEK
        glyphs += [0x0119] # LATIN SMALL LETTER E WITH OGONEK
        glyphs += [0x011A] # LATIN CAPITAL LETTER E WITH CARON
        glyphs += [0x011B] # LATIN SMALL LETTER E WITH CARON
        glyphs += [0x011C] # LATIN CAPITAL LETTER G WITH CIRCUMFLEX
        glyphs += [0x011D] # LATIN SMALL LETTER G WITH CIRCUMFLEX
        glyphs += [0x011E] # LATIN CAPITAL LETTER G WITH BREVE
        glyphs += [0x011F] # LATIN SMALL LETTER G WITH BREVE
        glyphs += [0x0120] # LATIN CAPITAL LETTER G WITH DOT ABOVE
        glyphs += [0x0121] # LATIN SMALL LETTER G WITH DOT ABOVE
        glyphs += [0x0122] # LATIN CAPITAL LETTER G WITH CEDILLA
        glyphs += [0x0123] # LATIN SMALL LETTER G WITH CEDILLA
        glyphs += [0x0124] # LATIN CAPITAL LETTER H WITH CIRCUMFLEX
        glyphs += [0x0125] # LATIN SMALL LETTER H WITH CIRCUMFLEX
        glyphs += [0x0126] # LATIN CAPITAL LETTER H WITH STROKE
        glyphs += [0x0127] # LATIN SMALL LETTER H WITH STROKE
        glyphs += [0x0128] # LATIN CAPITAL LETTER I WITH TILDE
        glyphs += [0x0129] # LATIN SMALL LETTER I WITH TILDE
        glyphs += [0x012A] # LATIN CAPITAL LETTER I WITH MACRON
        glyphs += [0x012B] # LATIN SMALL LETTER I WITH MACRON
        glyphs += [0x012E] # LATIN CAPITAL LETTER I WITH OGONEK
        glyphs += [0x012F] # LATIN SMALL LETTER I WITH OGONEK
        glyphs += [0x0130] # LATIN CAPITAL LETTER I WITH DOT ABOVE
        glyphs += [0x0131] # LATIN SMALL LETTER DOTLESS I
        glyphs += [0x0134] # LATIN CAPITAL LETTER J WITH CIRCUMFLEX
        glyphs += [0x0135] # LATIN SMALL LETTER J WITH CIRCUMFLEX
        glyphs += [0x0136] # LATIN CAPITAL LETTER K WITH CEDILLA
        glyphs += [0x0137] # LATIN SMALL LETTER K WITH CEDILLA
        glyphs += [0x0138] # LATIN SMALL LETTER KRA
        glyphs += [0x0139] # LATIN CAPITAL LETTER L WITH ACUTE
        glyphs += [0x013A] # LATIN SMALL LETTER L WITH ACUTE
        glyphs += [0x013B] # LATIN CAPITAL LETTER L WITH CEDILLA
        glyphs += [0x013C] # LATIN SMALL LETTER L WITH CEDILLA
        glyphs += [0x013D] # LATIN CAPITAL LETTER L WITH CARON
        glyphs += [0x013E] # LATIN SMALL LETTER L WITH CARON
        glyphs += [0x013F] # LATIN CAPITAL LETTER L WITH MIDDLE DOT
        glyphs += [0x0140] # LATIN SMALL LETTER L WITH MIDDLE DOT
        glyphs += [0x0141] # LATIN CAPITAL LETTER L WITH STROKE
        glyphs += [0x0142] # LATIN SMALL LETTER L WITH STROKE
        glyphs += [0x0143] # LATIN CAPITAL LETTER N WITH ACUTE
        glyphs += [0x0144] # LATIN SMALL LETTER N WITH ACUTE
        glyphs += [0x0145] # LATIN CAPITAL LETTER N WITH CEDILLA
        glyphs += [0x0146] # LATIN SMALL LETTER N WITH CEDILLA
        glyphs += [0x0147] # LATIN CAPITAL LETTER N WITH CARON
        glyphs += [0x0148] # LATIN SMALL LETTER N WITH CARON
        glyphs += [0x0149] # LATIN SMALL LETTER N PRECEDED BY APOSTROPHE
        glyphs += [0x014C] # LATIN CAPITAL LETTER O WITH MACRON
        glyphs += [0x014D] # LATIN SMALL LETTER O WITH MACRON
        glyphs += [0x0150] # LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
        glyphs += [0x0151] # LATIN SMALL LETTER O WITH DOUBLE ACUTE
        glyphs += [0x0152] # LATIN CAPITAL LIGATURE OE
        glyphs += [0x0153] # LATIN SMALL LIGATURE OE
        glyphs += [0x0154] # LATIN CAPITAL LETTER R WITH ACUTE
        glyphs += [0x0155] # LATIN SMALL LETTER R WITH ACUTE
        glyphs += [0x0156] # LATIN CAPITAL LETTER R WITH CEDILLA
        glyphs += [0x0157] # LATIN SMALL LETTER R WITH CEDILLA
        glyphs += [0x0158] # LATIN CAPITAL LETTER R WITH CARON
        glyphs += [0x0159] # LATIN SMALL LETTER R WITH CARON
        glyphs += [0x015A] # LATIN CAPITAL LETTER S WITH ACUTE
        glyphs += [0x015B] # LATIN SMALL LETTER S WITH ACUTE
        glyphs += [0x015C] # LATIN CAPITAL LETTER S WITH CIRCUMFLEX
        glyphs += [0x015D] # LATIN SMALL LETTER S WITH CIRCUMFLEX
        glyphs += [0x015E] # LATIN CAPITAL LETTER S WITH CEDILLA
        glyphs += [0x015F] # LATIN SMALL LETTER S WITH CEDILLA
        glyphs += [0x0160] # LATIN CAPITAL LETTER S WITH CARON
        glyphs += [0x0161] # LATIN SMALL LETTER S WITH CARON
        glyphs += [0x0162] # LATIN CAPITAL LETTER T WITH CEDILLA
        glyphs += [0x0163] # LATIN SMALL LETTER T WITH CEDILLA
        glyphs += [0x0164] # LATIN CAPITAL LETTER T WITH CARON
        glyphs += [0x0165] # LATIN SMALL LETTER T WITH CARON
        glyphs += [0x0168] # LATIN CAPITAL LETTER U WITH TILDE
        glyphs += [0x0169] # LATIN SMALL LETTER U WITH TILDE
        glyphs += [0x016A] # LATIN CAPITAL LETTER U WITH MACRON
        glyphs += [0x016B] # LATIN SMALL LETTER U WITH MACRON
        glyphs += [0x016C] # LATIN CAPITAL LETTER U WITH BREVE
        glyphs += [0x016D] # LATIN SMALL LETTER U WITH BREVE
        glyphs += [0x016E] # LATIN CAPITAL LETTER U WITH RING ABOVE
        glyphs += [0x016F] # LATIN SMALL LETTER U WITH RING ABOVE
        glyphs += [0x0170] # LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
        glyphs += [0x0171] # LATIN SMALL LETTER U WITH DOUBLE ACUTE
        glyphs += [0x0172] # LATIN CAPITAL LETTER U WITH OGONEK
        glyphs += [0x0173] # LATIN SMALL LETTER U WITH OGONEK
        glyphs += [0x0174] # LATIN CAPITAL LETTER W WITH CIRCUMFLEX
        glyphs += [0x0175] # LATIN SMALL LETTER W WITH CIRCUMFLEX
        glyphs += [0x0176] # LATIN CAPITAL LETTER Y WITH CIRCUMFLEX
        glyphs += [0x0177] # LATIN SMALL LETTER Y WITH CIRCUMFLEX
        glyphs += [0x0178] # LATIN CAPITAL LETTER Y WITH DIAERESIS
        glyphs += [0x0179] # LATIN CAPITAL LETTER Z WITH ACUTE
        glyphs += [0x017A] # LATIN SMALL LETTER Z WITH ACUTE
        glyphs += [0x017B] # LATIN CAPITAL LETTER Z WITH DOT ABOVE
        glyphs += [0x017C] # LATIN SMALL LETTER Z WITH DOT ABOVE
        glyphs += [0x017D] # LATIN CAPITAL LETTER Z WITH CARON
        glyphs += [0x017E] # LATIN SMALL LETTER Z WITH CARON
        glyphs += [0x018F] # LATIN CAPITAL LETTER SCHWA
        glyphs += [0x0192] # LATIN SMALL LETTER F WITH HOOK
        glyphs += [0x01A0] # LATIN CAPITAL LETTER O WITH HORN
        glyphs += [0x01A1] # LATIN SMALL LETTER O WITH HORN
        glyphs += [0x01AF] # LATIN CAPITAL LETTER U WITH HORN
        glyphs += [0x01B0] # LATIN SMALL LETTER U WITH HORN
        glyphs += [0x01CD] # LATIN CAPITAL LETTER A WITH CARON
        glyphs += [0x01CE] # LATIN SMALL LETTER A WITH CARON
        glyphs += [0x01CF] # LATIN CAPITAL LETTER I WITH CARON
        glyphs += [0x01D0] # LATIN SMALL LETTER I WITH CARON
        glyphs += [0x01D1] # LATIN CAPITAL LETTER O WITH CARON
        glyphs += [0x01D2] # LATIN SMALL LETTER O WITH CARON
        glyphs += [0x01D3] # LATIN CAPITAL LETTER U WITH CARON
        glyphs += [0x01D4] # LATIN SMALL LETTER U WITH CARON
        glyphs += [0x01D5] # LATIN CAPITAL LETTER U WITH DIAERESIS AND MACRON
        glyphs += [0x01D6] # LATIN SMALL LETTER U WITH DIAERESIS AND MACRON
        glyphs += [0x01D7] # LATIN CAPITAL LETTER U WITH DIAERESIS AND ACUTE
        glyphs += [0x01D8] # LATIN SMALL LETTER U WITH DIAERESIS AND ACUTE
        glyphs += [0x01D9] # LATIN CAPITAL LETTER U WITH DIAERESIS AND CARON
        glyphs += [0x01DA] # LATIN SMALL LETTER U WITH DIAERESIS AND CARON
        glyphs += [0x01DB] # LATIN CAPITAL LETTER U WITH DIAERESIS AND GRAVE
        glyphs += [0x01DC] # LATIN SMALL LETTER U WITH DIAERESIS AND GRAVE
        glyphs += [0x01E6] # LATIN CAPITAL LETTER G WITH CARON
        glyphs += [0x01E7] # LATIN SMALL LETTER G WITH CARON
        glyphs += [0x0218] # LATIN CAPITAL LETTER S WITH COMMA BELOW
        glyphs += [0x0219] # LATIN SMALL LETTER S WITH COMMA BELOW
        glyphs += [0x021A] # LATIN CAPITAL LETTER T WITH COMMA BELOW
        glyphs += [0x021B] # LATIN SMALL LETTER T WITH COMMA BELOW
        glyphs += [0x0237] # LATIN SMALL LETTER DOTLESS J
        glyphs += [0x0251] # LATIN SMALL LETTER ALPHA
        glyphs += [0x0259] # LATIN SMALL LETTER SCHWA
        glyphs += [0x0261] # LATIN SMALL LETTER SCRIPT G
        glyphs += [0x02BB] # MODIFIER LETTER TURNED COMMA
        glyphs += [0x02BC] # MODIFIER LETTER APOSTROPHE
        glyphs += [0x02BE] # MODIFIER LETTER RIGHT HALF RING
        glyphs += [0x02BF] # MODIFIER LETTER LEFT HALF RING
        glyphs += [0x02C6] # MODIFIER LETTER CIRCUMFLEX ACCENT
        glyphs += [0x02C7] # CARON
        glyphs += [0x02C8] # MODIFIER LETTER VERTICAL LINE
        glyphs += [0x02C9] # MODIFIER LETTER MACRON
        glyphs += [0x02CA] # MODIFIER LETTER ACUTE ACCENT
        glyphs += [0x02CB] # MODIFIER LETTER GRAVE ACCENT
        glyphs += [0x02CC] # MODIFIER LETTER LOW VERTICAL LINE
        glyphs += [0x02D8] # BREVE
        glyphs += [0x02D9] # DOT ABOVE
        glyphs += [0x02DA] # RING ABOVE
        glyphs += [0x02DB] # OGONEK
        glyphs += [0x02DC] # SMALL TILDE
        glyphs += [0x02DD] # DOUBLE ACUTE ACCENT
        glyphs += [0x0300] # COMBINING GRAVE ACCENT
        glyphs += [0x0301] # COMBINING ACUTE ACCENT
        glyphs += [0x0302] # COMBINING CIRCUMFLEX ACCENT
        glyphs += [0x0303] # COMBINING TILDE
        glyphs += [0x0304] # COMBINING MACRON
        glyphs += [0x0306] # COMBINING BREVE
        glyphs += [0x0307] # COMBINING DOT ABOVE
        glyphs += [0x0308] # COMBINING DIAERESIS
        glyphs += [0x0309] # COMBINING HOOK ABOVE
        glyphs += [0x030A] # COMBINING RING ABOVE
        glyphs += [0x030B] # COMBINING DOUBLE ACUTE ACCENT
        glyphs += [0x030C] # COMBINING CARON
        glyphs += [0x031B] # COMBINING HORN
        glyphs += [0x0323] # COMBINING DOT BELOW
        glyphs += [0x0324] # COMBINING DIAERESIS BELOW
        glyphs += [0x0326] # COMBINING COMMA BELOW
        glyphs += [0x0327] # COMBINING CEDILLA
        glyphs += [0x0328] # COMBINING OGONEK
        glyphs += [0x032E] # COMBINING BREVE BELOW
        glyphs += [0x0331] # COMBINING MACRON BELOW
        glyphs += [0x03C0] # GREEK SMALL LETTER PI
        glyphs += [0x1E0C] # LATIN CAPITAL LETTER D WITH DOT BELOW
        glyphs += [0x1E0D] # LATIN SMALL LETTER D WITH DOT BELOW
        glyphs += [0x1E0E] # LATIN CAPITAL LETTER D WITH LINE BELOW
        glyphs += [0x1E0F] # LATIN SMALL LETTER D WITH LINE BELOW
        glyphs += [0x1E20] # LATIN CAPITAL LETTER G WITH MACRON
        glyphs += [0x1E21] # LATIN SMALL LETTER G WITH MACRON
        glyphs += [0x1E24] # LATIN CAPITAL LETTER H WITH DOT BELOW
        glyphs += [0x1E25] # LATIN SMALL LETTER H WITH DOT BELOW
        glyphs += [0x1E2A] # LATIN CAPITAL LETTER H WITH BREVE BELOW
        glyphs += [0x1E2B] # LATIN SMALL LETTER H WITH BREVE BELOW
        glyphs += [0x1E36] # LATIN CAPITAL LETTER L WITH DOT BELOW
        glyphs += [0x1E37] # LATIN SMALL LETTER L WITH DOT BELOW
        glyphs += [0x1E38] # LATIN CAPITAL LETTER L WITH DOT BELOW AND MACRON
        glyphs += [0x1E39] # LATIN SMALL LETTER L WITH DOT BELOW AND MACRON
        glyphs += [0x1E3A] # LATIN CAPITAL LETTER L WITH LINE BELOW
        glyphs += [0x1E3B] # LATIN SMALL LETTER L WITH LINE BELOW
        glyphs += [0x1E42] # LATIN CAPITAL LETTER M WITH DOT BELOW
        glyphs += [0x1E43] # LATIN SMALL LETTER M WITH DOT BELOW
        glyphs += [0x1E44] # LATIN CAPITAL LETTER N WITH DOT ABOVE
        glyphs += [0x1E45] # LATIN SMALL LETTER N WITH DOT ABOVE
        glyphs += [0x1E46] # LATIN CAPITAL LETTER N WITH DOT BELOW
        glyphs += [0x1E47] # LATIN SMALL LETTER N WITH DOT BELOW
        glyphs += [0x1E48] # LATIN CAPITAL LETTER N WITH LINE BELOW
        glyphs += [0x1E49] # LATIN SMALL LETTER N WITH LINE BELOW
        glyphs += [0x1E5A] # LATIN CAPITAL LETTER R WITH DOT BELOW
        glyphs += [0x1E5B] # LATIN SMALL LETTER R WITH DOT BELOW
        glyphs += [0x1E5C] # LATIN CAPITAL LETTER R WITH DOT BELOW AND MACRON
        glyphs += [0x1E5D] # LATIN SMALL LETTER R WITH DOT BELOW AND MACRON
        glyphs += [0x1E5E] # LATIN CAPITAL LETTER R WITH LINE BELOW
        glyphs += [0x1E5F] # LATIN SMALL LETTER R WITH LINE BELOW
        glyphs += [0x1E60] # LATIN CAPITAL LETTER S WITH DOT ABOVE
        glyphs += [0x1E61] # LATIN SMALL LETTER S WITH DOT ABOVE
        glyphs += [0x1E62] # LATIN CAPITAL LETTER S WITH DOT BELOW
        glyphs += [0x1E63] # LATIN SMALL LETTER S WITH DOT BELOW
        glyphs += [0x1E6C] # LATIN CAPITAL LETTER T WITH DOT BELOW
        glyphs += [0x1E6D] # LATIN SMALL LETTER T WITH DOT BELOW
        glyphs += [0x1E6E] # LATIN CAPITAL LETTER T WITH LINE BELOW
        glyphs += [0x1E6F] # LATIN SMALL LETTER T WITH LINE BELOW
        glyphs += [0x1E80] # LATIN CAPITAL LETTER W WITH GRAVE
        glyphs += [0x1E81] # LATIN SMALL LETTER W WITH GRAVE
        glyphs += [0x1E82] # LATIN CAPITAL LETTER W WITH ACUTE
        glyphs += [0x1E83] # LATIN SMALL LETTER W WITH ACUTE
        glyphs += [0x1E84] # LATIN CAPITAL LETTER W WITH DIAERESIS
        glyphs += [0x1E85] # LATIN SMALL LETTER W WITH DIAERESIS
        glyphs += [0x1E8E] # LATIN CAPITAL LETTER Y WITH DOT ABOVE
        glyphs += [0x1E8F] # LATIN SMALL LETTER Y WITH DOT ABOVE
        glyphs += [0x1E92] # LATIN CAPITAL LETTER Z WITH DOT BELOW
        glyphs += [0x1E93] # LATIN SMALL LETTER Z WITH DOT BELOW
        glyphs += [0x1E97] # LATIN SMALL LETTER T WITH DIAERESIS
        glyphs += [0x1E9E] # LATIN CAPITAL LETTER SHARP S
        glyphs += [0x1EA0] # LATIN CAPITAL LETTER A WITH DOT BELOW
        glyphs += [0x1EA1] # LATIN SMALL LETTER A WITH DOT BELOW
        glyphs += [0x1EA2] # LATIN CAPITAL LETTER A WITH HOOK ABOVE
        glyphs += [0x1EA3] # LATIN SMALL LETTER A WITH HOOK ABOVE
        glyphs += [0x1EA4] # LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND ACUTE
        glyphs += [0x1EA5] # LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE
        glyphs += [0x1EA6] # LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND GRAVE
        glyphs += [0x1EA7] # LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE
        glyphs += [0x1EA8] # LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
        glyphs += [0x1EA9] # LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
        glyphs += [0x1EAA] # LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND TILDE
        glyphs += [0x1EAB] # LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE
        glyphs += [0x1EAC] # LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND DOT BELOW
        glyphs += [0x1EAD] # LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW
        glyphs += [0x1EAE] # LATIN CAPITAL LETTER A WITH BREVE AND ACUTE
        glyphs += [0x1EAF] # LATIN SMALL LETTER A WITH BREVE AND ACUTE
        glyphs += [0x1EB0] # LATIN CAPITAL LETTER A WITH BREVE AND GRAVE
        glyphs += [0x1EB1] # LATIN SMALL LETTER A WITH BREVE AND GRAVE
        glyphs += [0x1EB2] # LATIN CAPITAL LETTER A WITH BREVE AND HOOK ABOVE
        glyphs += [0x1EB3] # LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE
        glyphs += [0x1EB4] # LATIN CAPITAL LETTER A WITH BREVE AND TILDE
        glyphs += [0x1EB5] # LATIN SMALL LETTER A WITH BREVE AND TILDE
        glyphs += [0x1EB6] # LATIN CAPITAL LETTER A WITH BREVE AND DOT BELOW
        glyphs += [0x1EB7] # LATIN SMALL LETTER A WITH BREVE AND DOT BELOW
        glyphs += [0x1EB8] # LATIN CAPITAL LETTER E WITH DOT BELOW
        glyphs += [0x1EB9] # LATIN SMALL LETTER E WITH DOT BELOW
        glyphs += [0x1EBA] # LATIN CAPITAL LETTER E WITH HOOK ABOVE
        glyphs += [0x1EBB] # LATIN SMALL LETTER E WITH HOOK ABOVE
        glyphs += [0x1EBC] # LATIN CAPITAL LETTER E WITH TILDE
        glyphs += [0x1EBD] # LATIN SMALL LETTER E WITH TILDE
        glyphs += [0x1EBE] # LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND ACUTE
        glyphs += [0x1EBF] # LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE
        glyphs += [0x1EC0] # LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND GRAVE
        glyphs += [0x1EC1] # LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE
        glyphs += [0x1EC2] # LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
        glyphs += [0x1EC3] # LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
        glyphs += [0x1EC4] # LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND TILDE
        glyphs += [0x1EC5] # LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE
        glyphs += [0x1EC6] # LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND DOT BELOW
        glyphs += [0x1EC7] # LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW
        glyphs += [0x1EC8] # LATIN CAPITAL LETTER I WITH HOOK ABOVE
        glyphs += [0x1EC9] # LATIN SMALL LETTER I WITH HOOK ABOVE
        glyphs += [0x1ECA] # LATIN CAPITAL LETTER I WITH DOT BELOW
        glyphs += [0x1ECB] # LATIN SMALL LETTER I WITH DOT BELOW
        glyphs += [0x1ECC] # LATIN CAPITAL LETTER O WITH DOT BELOW
        glyphs += [0x1ECD] # LATIN SMALL LETTER O WITH DOT BELOW
        glyphs += [0x1ECE] # LATIN CAPITAL LETTER O WITH HOOK ABOVE
        glyphs += [0x1ECF] # LATIN SMALL LETTER O WITH HOOK ABOVE
        glyphs += [0x1ED0] # LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND ACUTE
        glyphs += [0x1ED1] # LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE
        glyphs += [0x1ED2] # LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND GRAVE
        glyphs += [0x1ED3] # LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE
        glyphs += [0x1ED4] # LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
        glyphs += [0x1ED5] # LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
        glyphs += [0x1ED6] # LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND TILDE
        glyphs += [0x1ED7] # LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE
        glyphs += [0x1ED8] # LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND DOT BELOW
        glyphs += [0x1ED9] # LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW
        glyphs += [0x1EDA] # LATIN CAPITAL LETTER O WITH HORN AND ACUTE
        glyphs += [0x1EDB] # LATIN SMALL LETTER O WITH HORN AND ACUTE
        glyphs += [0x1EDC] # LATIN CAPITAL LETTER O WITH HORN AND GRAVE
        glyphs += [0x1EDD] # LATIN SMALL LETTER O WITH HORN AND GRAVE
        glyphs += [0x1EDE] # LATIN CAPITAL LETTER O WITH HORN AND HOOK ABOVE
        glyphs += [0x1EDF] # LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE
        glyphs += [0x1EE0] # LATIN CAPITAL LETTER O WITH HORN AND TILDE
        glyphs += [0x1EE1] # LATIN SMALL LETTER O WITH HORN AND TILDE
        glyphs += [0x1EE2] # LATIN CAPITAL LETTER O WITH HORN AND DOT BELOW
        glyphs += [0x1EE3] # LATIN SMALL LETTER O WITH HORN AND DOT BELOW
        glyphs += [0x1EE4] # LATIN CAPITAL LETTER U WITH DOT BELOW
        glyphs += [0x1EE5] # LATIN SMALL LETTER U WITH DOT BELOW
        glyphs += [0x1EE6] # LATIN CAPITAL LETTER U WITH HOOK ABOVE
        glyphs += [0x1EE7] # LATIN SMALL LETTER U WITH HOOK ABOVE
        glyphs += [0x1EE8] # LATIN CAPITAL LETTER U WITH HORN AND ACUTE
        glyphs += [0x1EE9] # LATIN SMALL LETTER U WITH HORN AND ACUTE
        glyphs += [0x1EEA] # LATIN CAPITAL LETTER U WITH HORN AND GRAVE
        glyphs += [0x1EEB] # LATIN SMALL LETTER U WITH HORN AND GRAVE
        glyphs += [0x1EEC] # LATIN CAPITAL LETTER U WITH HORN AND HOOK ABOVE
        glyphs += [0x1EED] # LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE
        glyphs += [0x1EEE] # LATIN CAPITAL LETTER U WITH HORN AND TILDE
        glyphs += [0x1EEF] # LATIN SMALL LETTER U WITH HORN AND TILDE
        glyphs += [0x1EF0] # LATIN CAPITAL LETTER U WITH HORN AND DOT BELOW
        glyphs += [0x1EF1] # LATIN SMALL LETTER U WITH HORN AND DOT BELOW
        glyphs += [0x1EF2] # LATIN CAPITAL LETTER Y WITH GRAVE
        glyphs += [0x1EF3] # LATIN SMALL LETTER Y WITH GRAVE
        glyphs += [0x1EF4] # LATIN CAPITAL LETTER Y WITH DOT BELOW
        glyphs += [0x1EF5] # LATIN SMALL LETTER Y WITH DOT BELOW
        glyphs += [0x1EF6] # LATIN CAPITAL LETTER Y WITH HOOK ABOVE
        glyphs += [0x1EF7] # LATIN SMALL LETTER Y WITH HOOK ABOVE
        glyphs += [0x1EF8] # LATIN CAPITAL LETTER Y WITH TILDE
        glyphs += [0x1EF9] # LATIN SMALL LETTER Y WITH TILDE
        glyphs += [0x2007] # FIGURE SPACE
        glyphs += [0x2010] # HYPHEN
        glyphs += [0x2012] # FIGURE DASH
        glyphs += [0x2013] # EN DASH
        glyphs += [0x2014] # EM DASH
        glyphs += [0x2015] # HORIZONTAL BAR
        glyphs += [0x2018] # LEFT SINGLE QUOTATION MARK
        glyphs += [0x2019] # RIGHT SINGLE QUOTATION MARK
        glyphs += [0x201A] # SINGLE LOW-9 QUOTATION MARK
        glyphs += [0x201C] # LEFT DOUBLE QUOTATION MARK
        glyphs += [0x201D] # RIGHT DOUBLE QUOTATION MARK
        glyphs += [0x201E] # DOUBLE LOW-9 QUOTATION MARK
        glyphs += [0x2020] # DAGGER
        glyphs += [0x2021] # DOUBLE DAGGER
        glyphs += [0x2022] # BULLET
        glyphs += [0x2026] # HORIZONTAL ELLIPSIS
        glyphs += [0x2030] # PER MILLE SIGN
        glyphs += [0x2032] # PRIME
        glyphs += [0x2033] # DOUBLE PRIME
        glyphs += [0x2039] # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
        glyphs += [0x203A] # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
        glyphs += [0x2044] # FRACTION SLASH
        glyphs += [0x2070] # SUPERSCRIPT ZERO
        glyphs += [0x2074] # SUPERSCRIPT FOUR
        glyphs += [0x2075] # SUPERSCRIPT FIVE
        glyphs += [0x2076] # SUPERSCRIPT SIX
        glyphs += [0x2077] # SUPERSCRIPT SEVEN
        glyphs += [0x2078] # SUPERSCRIPT EIGHT
        glyphs += [0x2079] # SUPERSCRIPT NINE
        glyphs += [0x207D] # SUPERSCRIPT LEFT PARENTHESIS
        glyphs += [0x207E] # SUPERSCRIPT RIGHT PARENTHESIS
        glyphs += [0x207F] # SUPERSCRIPT LATIN SMALL LETTER N
        glyphs += [0x2080] # SUBSCRIPT ZERO
        glyphs += [0x2081] # SUBSCRIPT ONE
        glyphs += [0x2082] # SUBSCRIPT TWO
        glyphs += [0x2083] # SUBSCRIPT THREE
        glyphs += [0x2084] # SUBSCRIPT FOUR
        glyphs += [0x2085] # SUBSCRIPT FIVE
        glyphs += [0x2086] # SUBSCRIPT SIX
        glyphs += [0x2087] # SUBSCRIPT SEVEN
        glyphs += [0x2088] # SUBSCRIPT EIGHT
        glyphs += [0x2089] # SUBSCRIPT NINE
        glyphs += [0x208D] # SUBSCRIPT LEFT PARENTHESIS
        glyphs += [0x208E] # SUBSCRIPT RIGHT PARENTHESIS
        glyphs += [0x20A1] # COLON SIGN
        glyphs += [0x20A4] # LIRA SIGN
        glyphs += [0x20A6] # NAIRA SIGN
        glyphs += [0x20A7] # PESETA SIGN
        glyphs += [0x20AB] # DONG SIGN
        glyphs += [0x20AC] # EURO SIGN
        glyphs += [0x20B1] # PESO SIGN
        glyphs += [0x20B2] # GUARANI SIGN
        glyphs += [0x20B5] # CEDI SIGN
        glyphs += [0x2113] # SCRIPT SMALL L
        glyphs += [0x2117] # SOUND RECORDING COPYRIGHT
        glyphs += [0x2120] # SERVICE MARK
        glyphs += [0x2122] # TRADE MARK SIGN
        glyphs += [0x2126] # OHM SIGN
        glyphs += [0x212E] # ESTIMATED SYMBOL
        glyphs += [0x2153] # VULGAR FRACTION ONE THIRD
        glyphs += [0x2154] # VULGAR FRACTION TWO THIRDS
        glyphs += [0x215B] # VULGAR FRACTION ONE EIGHTH
        glyphs += [0x215C] # VULGAR FRACTION THREE EIGHTHS
        glyphs += [0x215D] # VULGAR FRACTION FIVE EIGHTHS
        glyphs += [0x215E] # VULGAR FRACTION SEVEN EIGHTHS
        glyphs += [0x2190] # LEFTWARDS ARROW
        glyphs += [0x2191] # UPWARDS ARROW
        glyphs += [0x2192] # RIGHTWARDS ARROW
        glyphs += [0x2193] # DOWNWARDS ARROW
        glyphs += [0x2202] # PARTIAL DIFFERENTIAL
        glyphs += [0x2206] # INCREMENT
        glyphs += [0x220F] # N-ARY PRODUCT
        glyphs += [0x2211] # N-ARY SUMMATION
        glyphs += [0x2212] # MINUS SIGN
        glyphs += [0x2215] # DIVISION SLASH
        glyphs += [0x2219] # BULLET OPERATOR
        glyphs += [0x221A] # SQUARE ROOT
        glyphs += [0x221E] # INFINITY
        glyphs += [0x222B] # INTEGRAL
        glyphs += [0x2248] # ALMOST EQUAL TO
        glyphs += [0x2260] # NOT EQUAL TO
        glyphs += [0x2264] # LESS-THAN OR EQUAL TO
        glyphs += [0x2265] # GREATER-THAN OR EQUAL TO
        glyphs += [0x25A0] # BLACK SQUARE
        glyphs += [0x25B2] # BLACK UP-POINTING TRIANGLE
        glyphs += [0x25B3] # WHITE UP-POINTING TRIANGLE
        glyphs += [0x25B6] # BLACK RIGHT-POINTING TRIANGLE
        glyphs += [0x25B7] # WHITE RIGHT-POINTING TRIANGLE
        glyphs += [0x25BC] # BLACK DOWN-POINTING TRIANGLE
        glyphs += [0x25BD] # WHITE DOWN-POINTING TRIANGLE
        glyphs += [0x25C0] # BLACK LEFT-POINTING TRIANGLE
        glyphs += [0x25C1] # WHITE LEFT-POINTING TRIANGLE
        glyphs += [0x25C6] # BLACK DIAMOND
        glyphs += [0x25CA] # LOZENGE
        glyphs += [0xFB01] # LATIN SMALL LIGATURE FI
        glyphs += [0xFB02] # LATIN SMALL LIGATURE FL
        return glyphs

library.register(Charmap)
