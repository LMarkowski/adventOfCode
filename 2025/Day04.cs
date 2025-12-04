namespace AdventOfCode2025;

public static class Day04
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 4 ===");
        string[] lines = File.ReadAllLines(test ? "inputs/day04_test.txt" : "inputs/day04.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static int[][] ToIntMatrix(string[] lines)
    {
        int[][] result = new int[lines.Length][];
        return lines.Select(line => line.Select(c => c == '@' ? 1 : 0).ToArray()).ToArray();
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        int[][] matrix = ToIntMatrix(lines);
        int result = CountRemovable(matrix, 4);
        Console.WriteLine($"Verified Result: {result}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        int[][] matrix = ToIntMatrix(lines);
        int initialCount = CountRolls(matrix);
        while (RemoveRolls(matrix, 4)) { } // Remove rolls until no more can be removed
        int finalCount = CountRolls(matrix);
        Console.WriteLine($"Result: {initialCount - finalCount}");
    }

    private static bool RemoveRolls(int[][] matrix, int maxAdjacent)
    {
        bool anyRemoved = false;
        ForEachCell(matrix, (i, j) =>
        {
            if (matrix[i][j] == 1 && SumAdjacent(matrix, i, j) < maxAdjacent)
            {
                matrix[i][j] = 0;
                anyRemoved = true;
            }
        });
        return anyRemoved;
    }

    private static int SumAdjacent(int[][] matrix, int row, int col)
    {
        int sum = 0;
        for (int i = -1; i <= 1; i++)
        {
            for (int j = -1; j <= 1; j++)
            {
                if (i == 0 && j == 0) continue;

                int newRow = row + i;
                int newCol = col + j;

                if (IsInBounds(matrix, newRow, newCol))
                    sum += matrix[newRow][newCol];
            }
        }
        return sum;
    }

    private static bool IsInBounds(int[][] matrix, int row, int col)
    {
        return row >= 0 && row < matrix.Length &&
               col >= 0 && col < matrix[0].Length;
    }

    private static bool ForEachCell(int[][] matrix, Action<int, int> action)
    {
        for (int i = 0; i < matrix.Length; i++)
        {
            for (int j = 0; j < matrix[i].Length; j++)
            {
                action(i, j);
            }
        }
        return true;
    }

    private static int CountRemovable(int[][] matrix, int maxAdjacent)
    {
        return CountCells(matrix, (i, j) => matrix[i][j] == 1 && SumAdjacent(matrix, i, j) < maxAdjacent);
    }

    private static int CountRolls(int[][] matrix)
    {
        return CountCells(matrix, (i, j) => matrix[i][j] == 1);
    }

    private static int CountCells(int[][] matrix, Func<int, int, bool> predicate)
    {
        int count = 0;
        ForEachCell(matrix, (i, j) => { if (predicate(i, j)) count++; });
        return count;
    }

}
