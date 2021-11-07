import utime

BIT7_MASK = 0b10000000
BIT6_MASK = 0b01000000
BIT5_MASK = 0b00100000
BIT4_MASK = 0b00010000
BIT3_MASK = 0b00001000
BIT2_MASK = 0b00000100
BIT1_MASK = 0b00000010
BIT0_MASK = 0b00000001

LCD_CLEAR = 0b00000001
LCD_HOME  = 0b00000010

LCD_RW_READ  = 1
LCD_RW_WRITE = 0

ENABLE_ON  = 1
ENABLE_OFF = 0

RS_DATA_SELECT        = 1
RS_INSTRUCTION_SELECT = 0

MODE_8_BITS = 1 # MODE_8_BITS: interfaces with LCD with 8 data bits at a time.
MODE_4_BITS = 0 # MODE_4_BITS: interfaces with LCD with two nibbles of 4 bits at a time.

class LiquidCrystalPico:
    def __init__(self, rs, e, d4, d5, d6, d7):
        self.rs = rs
        self.e  = e
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        self.__setup()

    def cursor_home(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(LCD_HOME, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)
        self.__delay()

    def cursor_move_forward(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00000110, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def cursor_move_back(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00000100, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def clear(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(LCD_CLEAR, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)
        self.__delay()

    def move_cursor_right(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00010100, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def move_cursor_left(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00010000, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def display_blink_on(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00001111, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def display_blink_off(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00001100, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def display_shift_text_right(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00011100, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def display_shift_text_left(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00011000, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def display_off(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00001000, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def display_on(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b00001100, MODE_8_BITS)
        self.rs.value(RS_DATA_SELECT)

    def move_to(self, line, column):
        shift = 0
        if (line == 0):
            shift = 0
        elif (line == 1):
            shift = 40
        elif (line == 2):
            shift = 20
        elif (line == 3):
            shift = 60

        self.cursor_home()
        for _ in range(0,shift+column):
            self.move_cursor_right()

    def __write_char(self, char, mode):
        if mode is MODE_8_BITS:
            self.d4.value((char & BIT4_MASK) >> 4)
            self.d5.value((char & BIT5_MASK) >> 5)
            self.d6.value((char & BIT6_MASK) >> 6)
            self.d7.value((char & BIT7_MASK) >> 7)
            self.__toggle_enable()

        self.d4.value((char & BIT0_MASK) >> 0)
        self.d5.value((char & BIT1_MASK) >> 1)
        self.d6.value((char & BIT2_MASK) >> 2)
        self.d7.value((char & BIT3_MASK) >> 3)
        self.__toggle_enable()

    def write(self, message):
        for char in message:
            self.__write_char(ord(char), MODE_8_BITS)
            self.__delay()

    def __toggle_enable(self):
        self.e.value(ENABLE_ON)
        self.__short_delay()
        self.e.value(ENABLE_OFF)
        self.__short_delay()

    def __setup(self):
        self.rs.value(RS_INSTRUCTION_SELECT)
        self.__write_char(0b0011, MODE_4_BITS)
        self.__write_char(0b0011, MODE_4_BITS)
        self.__write_char(0b0011, MODE_4_BITS)
        self.__write_char(0b0010, MODE_4_BITS)
        self.__write_char(0b00101000, MODE_8_BITS) # Function Set
        self.__write_char(0b00001100, MODE_8_BITS) # Display On/Off
        self.__write_char(0b00000110, MODE_8_BITS) # Entry Mode Set
        self.clear()
        self.rs.value(RS_DATA_SELECT)

    def __short_delay(self):
        utime.sleep_us(40)

    def __delay(self):
        utime.sleep_ms(2)

    def __long_delay(self):
        utime.sleep(0.3)