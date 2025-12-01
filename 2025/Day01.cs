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
        foreach (var line in lines)
        {
            Console.WriteLine(line);
        }
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
    }
}
