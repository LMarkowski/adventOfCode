namespace AdventOfCode2025;

public class Day07
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 7 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day07_test.txt" : "inputs/day07.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        char[][] map = DrawBeams(CharMap(lines));
        int result = CountSplits(map);
        Console.WriteLine($"Result: {result}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        char[][] map = DrawBeams(CharMap(lines));
        long[][] weights = CountBeamsWeights(map);
        long result = SumFinalWeights(weights);
        Console.WriteLine($"Result: {result}");
    }

    private static void PrintMap(char[][] map)
    {
        for (int i = 0; i < map.Length; i++)
        {
            for (int j = 0; j < map[i].Length; j++)
            {
                Console.Write(map[i][j]);
            }
            Console.WriteLine();
        }
    }

    private static char[][] CharMap(string[] lines)
    {
        char[][] map = new char[lines.Length][];

        for (int i = 0; i < lines.Length; i++)
        {
            char[] tmp = new char[lines[i].Length];
            for (int j = 0; j < lines[i].Length; j++)
                tmp[j] = lines[i].ElementAt(j);
            map[i] = tmp;
        }
        return map;
    }

    private static char[][] DrawBeams(char[][] map)
    {
        for (int i = 1; i < map.Length; i++)
        {
            for (int j = 0; j < map[i].Length; j++)
            {
                if (map[i - 1][j] == 'S')
                    map[i][j] = '|';
                else if (map[i - 1][j] == '|')
                {
                    if (map[i][j] == '^')
                    {
                        map[i][j - 1] = '|';
                        map[i][j + 1] = '|';
                    }
                    else
                        map[i][j] = '|';
                }
            }
        }
        return map;
    }

    private static int CountSplits(char[][] map)
    {
        int result = 0;
        for (int i = 1; i < map.Length; i++)
            for (int j = 0; j < map[i].Length; j++)
                if (map[i][j] == '^' && map[i - 1][j] == '|')
                    result++;
        return result;
    }

    private static long[][] CountBeamsWeights(char[][] map)
    {
        long[][] weights = map.Select(row => new long[row.Length]).ToArray();

        for (int i = 1; i < map.Length; i++)
        {
            for (int j = 0; j < map[i].Length; j++)
            {
                if (map[i - 1][j] == 'S')
                    weights[i][j] = 1;

                if (map[i][j] == '|')
                {
                    weights[i][j] += weights[i - 1][j];
                    if (j > 0 && map[i][j - 1] == '^')
                        weights[i][j] += weights[i - 1][j - 1];
                    if (j < map[i].Length - 1 && map[i][j + 1] == '^')
                        weights[i][j] += weights[i - 1][j + 1];
                }
            }
        }
        return weights;
    }

    private static long SumFinalWeights(long[][] weights) =>
        weights[^1].Sum();
}
