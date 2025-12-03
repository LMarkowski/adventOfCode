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

        int day = int.Parse(args[0]);
        bool test = args.Length > 1 && args[1] == "test";

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
            default:
                Console.WriteLine($"Day {day} not implemented yet.");
                break;
        }
    }
}
