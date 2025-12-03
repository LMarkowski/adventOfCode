namespace AdventOfCode2025;

public static class Day03
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 3 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day03_test.txt" : "inputs/day03.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        long sum = lines.Sum(bank => bank.ToDigits().MaxPossibleJoltage(2));
        Console.WriteLine(sum);
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        long sum = lines.Sum(bank => bank.ToDigits().MaxPossibleJoltage(12));
        Console.WriteLine(sum);
    }

    private static int[] ToDigits(this string bank)
    {
        return [.. bank.Select(c => c - '0')];
    }

    private static long MaxPossibleJoltage(this int[] digits, int batteryCount)
    {
        long result = 0;
        int startIndex = 0;

        for (int i = batteryCount - 1; i >= 0; i--)
        {
            int maxDigit = 0;
            int maxIndex = startIndex;

            for (int index = startIndex; index <= digits.Length - i - 1; index++)
            {
                if (digits[index] > maxDigit)
                {
                    maxDigit = digits[index];
                    maxIndex = index;
                }
            }

            result += maxDigit * (long)Math.Pow(10, i);
            startIndex = maxIndex + 1;
        }

        return result;
    }

}

