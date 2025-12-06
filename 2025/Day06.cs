using System.Net.NetworkInformation;
using System.Runtime.Serialization.Formatters;

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

    private static long[][] GetNumbers(string[][] matrix)
    {
        // Last element is the math operation, so ignore it
        int rowCount = matrix.Length;
        int colCount = matrix[0].Length - 1;
        long[][] numberMatrix = new long[rowCount][];

        for (int r = 0; r < rowCount; r++)
        {
            numberMatrix[r] = new long[colCount];
            for (int c = 0; c < colCount; c++)
            {
                numberMatrix[r][c] = long.Parse(matrix[r][c]);
            }
        }
        return numberMatrix;

    }

    private static string[][] TransposeMatrix(string[][] matrix)
    {
        int rowCount = matrix.Length;
        int colCount = matrix[0].Length;
        string[][] transposed = new string[colCount][];

        for (int c = 0; c < colCount; c++)
        {
            transposed[c] = new string[rowCount];
            for (int r = 0; r < rowCount; r++)
            {
                transposed[c][r] = matrix[r][c];
            }
        }
        return transposed;
    }

    private static char[][] TransposeMatrix(char[][] matrix)
    {
        int rowCount = matrix.Length;
        int colCount = matrix[0].Length;
        char[][] transposed = new char[colCount][];

        for (int c = 0; c < colCount; c++)
        {
            transposed[c] = new char[rowCount];
            for (int r = 0; r < rowCount; r++)
            {
                transposed[c][r] = matrix[r][c];
            }
        }
        return transposed;
    }

    private static char[][] CharMatrix(string[] matrix)
    {
        int rowCount = matrix.Length;
        int colCount = matrix[0].Length;
        char[][] charMatrix = new char[rowCount][];
        for (int r = 0; r < rowCount; r++)
        {
            charMatrix[r] = new char[colCount];
            for (int c = 0; c < colCount; c++)
            {
                charMatrix[r][c] = matrix[r][c];
            }
        }
        return charMatrix;
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        string[][] stringMatrix = GetStrings(lines);
        string[][] transposedMatrix = TransposeMatrix(stringMatrix);

        long[][] numbers = GetNumbers(transposedMatrix);
        char[] operations = transposedMatrix.Select(row => row[^1][0]).ToArray();

        long result = 0;

        for (int i = 0; i < numbers.Length; i++)
        {
            long columnResult = CalcuateColumnResult(numbers[i], operations[i]);
            result += columnResult;
        }
        Console.WriteLine($"Result: {result}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        char[][] charMatrix = TransposeMatrix(CharMatrix(lines));

        long[][] numbers = new long[charMatrix.Length][];
        List<char> operations = new List<char>();


        // Get numbers and operations
        for (int r = 0; r < charMatrix.Length; r++)
        {

            List<long> numberList = new List<long>();
            string number_s = "";

            for (int c = 0; c < charMatrix[r].Length; c++)
            {
                if (char.IsDigit(charMatrix[r][c]))
                {
                    number_s += charMatrix[r][c];
                }
                else if (charMatrix[r][c] == '+' || charMatrix[r][c] == '*')
                {
                    operations.Add(charMatrix[r][c]);
                }
            }
            if (number_s.Length > 0)
                numberList.Add(long.Parse(number_s));

            numbers[r] = numberList.ToArray();

        }

        // After parsing numbers, group them by splitting on empty arrays
        List<List<long>> groupedNumbers = new List<List<long>>();
        List<long> currentGroup = new List<long>();

        for (int r = 0; r < numbers.Length; r++)
        {
            if (numbers[r].Length == 0)
            {
                // Empty array - save current group and start new one
                if (currentGroup.Count > 0)
                {
                    groupedNumbers.Add(new List<long>(currentGroup));
                    currentGroup.Clear();
                }
            }
            else
            {
                // Add all numbers from this row to current group
                currentGroup.AddRange(numbers[r]);
            }
        }

        // Don't forget the last group
        if (currentGroup.Count > 0)
        {
            groupedNumbers.Add(currentGroup);
        }

        long result = 0;
        for (int i = 0; i < groupedNumbers.Count; i++)
        {
            long columnResult = CalcuateColumnResult(groupedNumbers[i].ToArray(), operations[i]);
            result += columnResult;
        }
        Console.WriteLine($"Result: {result}");
    }

    private static long CalcuateColumnResult(long[] numbers, char operation)
    {
        long columnResult = numbers[0];
        for (int j = 1; j < numbers.Length; j++)
        {
            switch (operation)
            {
                case '+':
                    columnResult += numbers[j];
                    break;
                case '*':
                    columnResult *= numbers[j];
                    break;
                default:
                    throw new Exception($"Unknown operation: {operation}");
            }
        }
        return columnResult;
    }
}
