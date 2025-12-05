namespace AdventOfCode2025;

public class Day05
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 5 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day05_test.txt" : "inputs/day05.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static List<(long start, long end)> ParseRanges(string[] lines)
    {
        return lines
            .TakeWhile(line => !string.IsNullOrWhiteSpace(line))
            .Select(line => line.Split('-'))
            .Select(parts => (long.Parse(parts[0]), long.Parse(parts[1])))
            .ToList();
    }

    private static List<long> ParseIds(string[] lines)
    {
        return lines
            .SkipWhile(line => !string.IsNullOrWhiteSpace(line))
            .Skip(1) // Skip the blank line itself
            .Select(long.Parse)
            .ToList();
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        List<(long start, long end)> ranges = ParseRanges(lines);
        List<long> ids = ParseIds(lines);
        int result = ids.Count(id => ranges.Any(range => id >= range.start && id <= range.end));

        Console.WriteLine($"Result: {result}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        List<(long start, long end)> ranges = ParseRanges(lines);
        ranges = MergeOverlappingRanges(ranges);
        long sum = ranges.Sum(range => range.end - range.start + 1);

        Console.WriteLine($"Result: {sum}");
    }


    private static List<(long start, long end)> MergeOverlappingRanges(List<(long start, long end)> ranges)
    {
        if (ranges.Count == 0) return ranges;

        var sorted = ranges.OrderBy(r => r.start).ToList();
        var result = new List<(long start, long end)> { sorted[0] };

        foreach (var next in sorted.Skip(1))
        {
            var current = result[^1];
            if (next.start <= current.end + 1)
                result[^1] = (current.start, Math.Max(current.end, next.end));
            else
                result.Add(next);
        }
        return result;
    }
}