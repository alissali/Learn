class Color:
    # Foreground
    F_Default = "\x1b[39m"
    F_Black = "\x1b[30m"
    F_Red = "\x1b[31m"
    F_Green = "\x1b[32m"
    F_Yellow = "\x1b[33m"
    F_Blue = "\x1b[34m"
    F_Magenta = "\x1b[35m"
    F_Cyan = "\x1b[36m"
    F_LightGray = "\x1b[37m"
    F_DarkGray = "\x1b[90m"
    F_LightRed = "\x1b[91m"
    F_LightGreen = "\x1b[92m"
    F_LightYellow = "\x1b[93m"
    F_LightBlue = "\x1b[94m"
    F_LightMagenta = "\x1b[95m"
    F_LightCyan = "\x1b[96m"
    F_White = "\x1b[97m"
    # Background
    B_Default = "\x1b[49m"
    B_Black = "\x1b[40m"
    B_Red = "\x1b[41m"
    B_Green = "\x1b[42m"
    B_Yellow = "\x1b[43m"
    B_Blue = "\x1b[44m"
    B_Magenta = "\x1b[45m"
    B_Cyan = "\x1b[46m"
    B_LightGray = "\x1b[47m"
    B_DarkGray = "\x1b[100m"
    B_LightRed = "\x1b[101m"
    B_LightGreen = "\x1b[102m"
    B_LightYellow = "\x1b[103m"
    B_LightBlue = "\x1b[104m"
    B_LightMagenta = "\x1b[105m"
    B_LightCyan = "\x1b[106m"
    B_White = "\x1b[107m"
    
    def __str__(self):
        return self.currentColor
        
    @classmethod
    def getColor(self, color):
        self.currentColor = self.__getattribute__(self, color)
        print(self.currentColor)
    
def main():
    pass

if __name__ == '__main__':
    main()
