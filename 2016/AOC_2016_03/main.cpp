#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#include <sstream>

int main()
{
    vector<string> input;

    ifstream inputFile("input.txt");
    if (inputFile.is_open())
    {
        string line;
        while (getline(inputFile, line))
        {
            input.push_back(line);
        }
        inputFile.close();
    }
    else
    {
        cout << "Unable to open file" << endl;
    }

    vector<vector<int> > lengths;

    for (string line : input)
    {
        stringstream ss(line);
        string token;
        vector<int> tokens;
        while (getline(ss, token, ' '))
        {
            if (token != "" && token != " " && token != "\n" && token != "\t" && token != "\r")
            {
                tokens.push_back(stoi(token));
            }
        }

        lengths.push_back(tokens);
    }

    int not_triangles = 0, triangles = 0;

    for (vector<int> trio : lengths)
    {
        if (trio[0] + trio[1] > trio[2] && trio[0] + trio[2] > trio[1] && trio[1] + trio[2] > trio[0])
        {
            triangles++;
        }
        else
        {
            not_triangles++;
        }
    }

    cout << "Triangles: " << triangles << endl;
    cout << "Not triangles: " << not_triangles << endl;

    // part 2

    not_triangles = 0;
    triangles = 0;

    for (int i = 0; i < lengths.size(); i += 3)
    {
        for (int j = 0; j < 3; j++)
        {
            vector<int> trio;
            trio.push_back(lengths[i][j]);
            trio.push_back(lengths[i + 1][j]);
            trio.push_back(lengths[i + 2][j]);

            if (trio[0] + trio[1] > trio[2] && trio[0] + trio[2] > trio[1] && trio[1] + trio[2] > trio[0])
            {
                triangles++;
            }
            else
            {
                not_triangles++;
            }
        }
    }

    cout << "Part 2" << endl;
    cout << "Triangles: " << triangles << endl;
    cout << "Not triangles: " << not_triangles << endl;

    return 0;
}
