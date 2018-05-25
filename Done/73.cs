// Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
// If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
// 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
// It can be seen that there are 3 fractions between 1/3 and 1/2.
// How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

int upperlimit = 12000;

int a = 0;
int b = 1;
int c = 1;
int d = upperlimit;
List<Tuple<int, int>> FareySeq = new List<Tuple<int, int>>();
FareySeq.Add(Tuple.Create(a, b));

int inrangecount = 0;

while (c < upperlimit)
{
    int k = (upperlimit + b) / d;
    int new_a = c;
    int new_b = d;
    c = (k*c-a);
    d = (k*d-b);
    FareySeq.Add(Tuple.Create(new_a, new_b));
    a = new_a;
    b = new_b;

    double fraction_value = (double) a / (double) b;
    double one_third = 1.0 / 3.0;
    double one_half = 1.0 / 2.0;
    if (fraction_value > one_third && fraction_value < one_half) {
        inrangecount += 1;
    }
}

Console.WriteLine(FareySeq.Count)
Console.WriteLine(inrangecount)