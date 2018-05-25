// Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

// However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

// Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

// NOTE: The first two lines in the file represent the numbers in the example given above.

// Get the exponent times the log of the base, compare that
Console.WriteLine(518061 * Math.Log(632382) > 525806 * Math.Log(519432))
Console.WriteLine(11 * Math.Log(2) < 7 * Math.Log(3))

string[] lines = System.IO.File.ReadAllLines(@"./99.input.txt");
double curr_max = 0;
int max_line = 0;
for (int i = 0; i < lines.Length; i +=1){
    string[] numbers_text = lines[i].Split(',');
    int bas = int.Parse(numbers_text[0]);
    int exp = int.Parse(numbers_text[1]);
    double this_val = (double) exp * Math.Log(bas);
    if (this_val > curr_max) {
        curr_max = this_val;
        max_line = i + 1; // answer is line number, not index...
    }
}

Console.WriteLine(max_line)
