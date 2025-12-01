namespace AdventOfCode2025;

public class Day01
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 1 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day01_test.txt" : "inputs/day01.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        int result = CountZeroCrossings(lines, false);
        Console.WriteLine($"Result: {result}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        int result = CountZeroCrossings(lines, true);
        Console.WriteLine($"Result: {result}");
    }

    private static int CountZeroCrossings(string[] lines, bool countEachStep)
    {
        int result = 0;
        int pos = 50;

        foreach (var line in lines)
        {
            char direction = line[0];
            int distance = int.Parse(line.Substring(1));
            int steps = countEachStep ? distance : 1;
            int move = countEachStep ? 1 : distance;

            for (int i = 0; i < steps; i++)
            {
                pos += direction == 'R' ? move : -move;
                pos = (pos + 100) % 100;
                if (pos == 0)
                    result++;
            }
        }

        return result;
    }
}