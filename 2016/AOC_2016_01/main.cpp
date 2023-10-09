#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Direction
{
    North,
    East,
    South,
    West
};

int main()
{
    string input;

    ifstream inputFile("input.txt");
    if (inputFile.is_open())
    {
        string line;
        while (getline(inputFile, line))
        {
            input = line;
        }
        inputFile.close();
    }
    else
    {
        cout << "Unable to open file" << endl;
    }

    vector<string> instructions;
    size_t start = 0, end;

    // Split the input string into individual instructions
    while ((end = input.find(", ", start)) != string::npos)
    {
        instructions.push_back(input.substr(start, end - start));
        start = end + 2;
    }
    instructions.push_back(input.substr(start));

    int x = 0, y = 0;         // Starting position
    Direction facing = North; // Starting direction

    for (const string &instruction : instructions)
    {
        char turn = instruction[0];
        int distance = stoi(instruction.substr(1));

        // Update direction based on turn
        if (turn == 'R')
        {
            facing = static_cast<Direction>((facing + 1) % 4);
        }
        else
        {
            facing = static_cast<Direction>((facing + 3) % 4);
        }

        // Update position based on direction
        switch (facing)
        {
        case North:
            y += distance;
            break;
        case East:
            x += distance;
            break;
        case South:
            y -= distance;
            break;
        case West:
            x -= distance;
            break;
        }
    }

    // Calculate Manhattan distance from starting position to final position
    int distance = abs(x) + abs(y);

    cout << "Shortest distance to the destination: " << distance << " blocks" << endl;

    // Part 2

    x = 0, y = 0;
    facing = North;
    vector<pair<int, int>> visited;
    visited.push_back(make_pair(x, y));

    for (const string &instruction : instructions)
    {
        char turn = instruction[0];
        int distance = stoi(instruction.substr(1));

        // Update direction based on turn
        if (turn == 'R')
        {
            facing = static_cast<Direction>((facing + 1) % 4);
        }
        else
        {
            facing = static_cast<Direction>((facing + 3) % 4);
        }

        // Update position based on direction
        for (int i = 0; i < distance; ++i)
        {
            switch (facing)
            {
            case North:
                y += 1;
                break;
            case East:
                x += 1;
                break;
            case South:
                y -= 1;
                break;
            case West:
                x -= 1;
                break;
            }
            if (find(visited.begin(), visited.end(), make_pair(x, y)) != visited.end())
            {
                int distance = abs(x) + abs(y);
                cout << "Shortest distance to the first location you visit twice: " << distance << " blocks" << endl;
                return 0;
            }
            else
            {
                visited.push_back(make_pair(x, y));
            }
        }
    }

    return 0;
}
