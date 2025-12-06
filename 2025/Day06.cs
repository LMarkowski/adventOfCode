namespace AdventOfCode2025;

public class Day06
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 6 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day06_test.txt" : "inputs/day06.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static string[][] GetStrings(string[] lines)
    {
        return lines.Select(line => line.Split(null as char[], StringSplitOptions.RemoveEmptyEntries)).ToArray();
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        string[][] stringMatrix = GetStrings(lines);
        string[][] transposedMatrix = TransposeMatrix(stringMatrix);

        long result = 0;

        for (int i = 0; i < transposedMatrix.Length; i++)
        {
            long[] numbers = transposedMatrix[i][..^1].Select(long.Parse).ToArray();
            char operation = transposedMatrix[i][^1][0];

            long columnResult = CalcuateColumnResult(numbers, operation);
            result += columnResult;
        }
        Console.WriteLine($"Result: {result}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        char[][] charMatrix = TransposeMatrix(lines.Select(line => line.ToCharArray()).ToArray());
        var (numbers, operations) = ParseNumbersAndOperationsForPart2(charMatrix);

        long result = 0;
        for (int i = 0; i < numbers.Count; i++)
        {
            long columnResult = CalcuateColumnResult(numbers[i].ToArray(), operations[i]);
            result += columnResult;
        }
        Console.WriteLine($"Result: {result}");
    }

    private static (List<List<long>> numbers, List<char> operations) ParseNumbersAndOperationsForPart2(char[][] charMatrix)
    {
        List<List<long>> numbers = new List<List<long>>();
        List<char> operations = new List<char>();

        List<long> currentList = new List<long>();
        for (int r = 0; r < charMatrix.Length; r++)
        {
            if (charMatrix[r].All(c => char.IsWhiteSpace(c)))
            {
                numbers.Add(currentList);
                currentList = new List<long>();
                continue;
            }
            string number_s = "";
            for (int c = 0; c < charMatrix[r].Length; c++)
            {
                if (char.IsDigit(charMatrix[r][c]))
                    number_s += charMatrix[r][c];
                else if (charMatrix[r][c] == '+' || charMatrix[r][c] == '*')
                    operations.Add(charMatrix[r][c]);
            }
            if (number_s.Length > 0)
                currentList.Add(long.Parse(number_s));
        }

        if (currentList.Count > 0)
            numbers.Add(currentList);

        return (numbers, operations);
    }

    private static long CalcuateColumnResult(long[] numbers, char operation)
    {
        long result = numbers[0];
        for (int j = 1; j < numbers.Length; j++)
        {
            result = operation == '+' ? result + numbers[j] : result * numbers[j];

        }
        return result;
    }

    private static T[][] TransposeMatrix<T>(T[][] matrix)
    {
        int rowCount = matrix.Length;
        int colCount = matrix[0].Length;
        T[][] transposed = new T[colCount][];

        for (int c = 0; c < colCount; c++)
        {
            transposed[c] = new T[rowCount];
            for (int r = 0; r < rowCount; r++)
            {
                transposed[c][r] = matrix[r][c];
            }
        }
        return transposed;
    }

}
