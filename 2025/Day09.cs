using System.Diagnostics.CodeAnalysis;
using System.IO.Pipelines;

namespace AdventOfCode2025;

public class Day09
{
    public static void Solve(bool test)
    {
        Console.WriteLine("=== Day 9 ===");

        string[] lines = File.ReadAllLines(test ? "inputs/day09_test.txt" : "inputs/day09.txt");

        SolvePart1(lines);
        SolvePart2(lines);
    }

    private static void SolvePart1(string[] lines)
    {
        Console.WriteLine("Part 1:");
        var corners = new List<Point>();
        foreach (string line in lines)
        {
            string[] coords = line.Split(",");
            corners.Add(new Point(long.Parse(coords[0]), long.Parse(coords[1])));
        }

        long maxArea = 0;
        for (int i = 0; i < corners.Count; i++)
        {
            for (int j = i + 1; j < corners.Count; j++)
            {
                Rectangle r = new(corners[i], corners[j]);
                long area = Rectangle.Area(r);
                if (area > maxArea)
                {
                    maxArea = area;
                }
            }
        }
        Console.WriteLine($"Result: {maxArea}");
    }

    private static void SolvePart2(string[] lines)
    {
        Console.WriteLine("Part 2:");
        var corners = new List<Point>();
        foreach (string line in lines)
        {
            string[] coords = line.Split(",");
            corners.Add(new Point(long.Parse(coords[0]), long.Parse(coords[1])));
        }

        long maxArea = 0;
        for (int i = 0; i < corners.Count; i++)
        {
            for (int j = i + 1; j < corners.Count; j++)
            {
                Rectangle r = new(corners[i], corners[j]);
                if (!Rectangle.IsInsidePolygon(r, corners))
                    continue;
                long area = Rectangle.Area(r);
                if (area > maxArea)
                    maxArea = area;
            }
        }
        Console.WriteLine($"Result: {maxArea}");
    }

    private static bool IsInside(Point p, List<Point> polygon)
    {
        int n = polygon.Count;

        // Check if point is on any edge
        for (int i = 0; i < n; i++)
        {
            Point p1 = polygon[i];
            Point p2 = polygon[(i + 1) % n];

            if (IsOnSegment(p, p1, p2))
                return true;
        }

        // Ray casting for interior points
        int intersections = 0;

        for (int i = 0; i < n; i++)
        {
            Point p1 = polygon[i];
            Point p2 = polygon[(i + 1) % n];

            if ((p1.Y > p.Y) != (p2.Y > p.Y))
            {
                long intersectionX = p1.X + (p.Y - p1.Y) * (p2.X - p1.X) / (p2.Y - p1.Y);

                if (p.X < intersectionX)
                {
                    intersections++;
                }
            }
        }

        return intersections % 2 == 1;
    }

    private static bool IsOnSegment(Point p, Point p1, Point p2)
    {
        // Check if p is collinear with p1 and p2
        long crossProduct = (p.Y - p1.Y) * (p2.X - p1.X) - (p.X - p1.X) * (p2.Y - p1.Y);

        if (crossProduct != 0)
            return false;

        // Check if p is within the bounding box of the segment
        return p.X >= Math.Min(p1.X, p2.X) && p.X <= Math.Max(p1.X, p2.X) &&
               p.Y >= Math.Min(p1.Y, p2.Y) && p.Y <= Math.Max(p1.Y, p2.Y);
    }


    public class Point(long x, long y)
    {
        public long X = x;
        public long Y = y;

        public static long ManhattanDistance(Point a, Point b)
        {
            return Math.Abs(a.X - b.X) + Math.Abs(a.Y - b.Y);
        }
    }

    public class Rectangle(Point c1, Point c2)
    {
        public Point corner1 = c1;
        public Point corner2 = c2;

        public static long Area(Rectangle r)
        {
            return (Math.Abs(r.corner1.X - r.corner2.X) + 1) * (Math.Abs(r.corner1.Y - r.corner2.Y) + 1);
        }

        public static bool IsInsidePolygon(Rectangle r, List<Point> polygon)
        {
            List<Point> corners = new List<Point>([r.corner1, r.corner2]);
            long minX = corners.Min(c => c.X);
            long maxX = corners.Max(c => c.X);
            long minY = corners.Min(c => c.Y);
            long maxY = corners.Max(c => c.Y);


            for (long x = minX; x <= maxX; x++)
                for (long y = minY; y <= maxY; y++)
                    if (!IsInside(new Point(x, y), polygon))
                        return false;

            return true;
        }

    }

    public static void PrintTiles(List<Point> red, List<Point> green)
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 13; j++)
            {
                if (red.Any(p => p.X == j && p.Y == i))
                    Console.Write('#');
                else if (green.Any(p => p.X == j && p.Y == i))
                    Console.Write('X');
                else
                    Console.Write('.');
            }
            Console.WriteLine();
        }
    }
}
