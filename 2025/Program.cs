using System.ComponentModel.DataAnnotations;

namespace AdventOfCode2025;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Usage: dotnet run <day>");
            Console.WriteLine("Example: dotnet run 1");
            Console.WriteLine("Add 'test' as second argument to run with test input.");
            return;
        }

        if (args[0] == "all")
        {
            for (int i = 1; i <= 12; i++)
            {
                bool t = args.Length > 1 && args[1] == "test";
                RunDay(i, t);
            }
            return;
        }
        int day = int.Parse(args[0]);
        bool test = args.Length > 1 && args[1] == "test";

        RunDay(day, test);
    }

    private static void RunDay(int day, bool test)
    {
        switch (day)
        {
            case 1:
                Day01.Solve(test);
                break;
            case 2:
                Day02.Solve(test);
                break;
            case 3:
                Day03.Solve(test);
                break;
            case 4:
                Day04.Solve(test);
                break;
            case 5:
                Day05.Solve(test);
                break;
            case 6:
                Day06.Solve(test);
                break;
            case 7:
                Day07.Solve(test);
                break;
            case 8:
                Day08.Solve(test);
                break;
            case 9:
                Day09.Solve(test);
                break;
            case 10:
                Day10.Solve(test);
                break;
            case 11:
                Day11.Solve(test);
                break;
            case 12:
                Day12.Solve(test);
                break;
            default:
                Console.WriteLine($"Day {day} not implemented yet.");
                break;
        }
    }
}
