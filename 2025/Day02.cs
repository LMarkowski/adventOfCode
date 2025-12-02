namespace AdventOfCode2025;

public class Day02
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 2 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day02_test.txt" : "inputs/day02.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static List<(long start, long end)> ParseRanges(string[] lines)
    {
        return lines[0].Split(',')
            .Select(range => range.Split('-'))
            .Select(bounds => (long.Parse(bounds[0]), long.Parse(bounds[1])))
            .ToList();
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        List<(long start, long end)> ranges = ParseRanges(lines);
        long sum = 0;
        foreach ((long start, long end) in ranges)
            for (long current_id = start; current_id <= end; current_id++)
                if (HasEqualHalves(current_id))
                    sum += current_id;

        Console.WriteLine(sum);
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        List<(long start, long end)> ranges = ParseRanges(lines);

        long sum = 0;
        foreach ((long start, long end) in ranges)
            for (long current_id = start; current_id <= end; current_id++)
                if (HasRepeatingPattern(current_id))
                    sum += current_id;

        Console.WriteLine(sum);
    }

    private static bool HasEqualHalves(long id)
    {
        string idStr = id.ToString();
        if (idStr.Length % 2 != 0)
            return false;

        int mid = idStr.Length / 2;
        string left = idStr[..mid];
        string right = idStr[mid..];

        return left == right;
    }


    private static bool HasRepeatingPattern(long id)
    {
        string idString = id.ToString();
        for (int patternLength = 1; patternLength <= idString.Length / 2; patternLength++)
        {
            if (idString.Length % patternLength != 0)
                continue;
            if (IsRepeatingPattern(idString, patternLength))
                return true;
        }
        return false;
    }

    private static bool IsRepeatingPattern(string id, int patternLength)
    {
        string pattern = id[..patternLength];
        int repetitions = id.Length / patternLength;
        for (int i = 1; i < repetitions; i++)
        {
            string segmet = id.Substring(i * patternLength, patternLength);
            if (segmet != pattern)
                return false;
        }
        return true;
    }
}