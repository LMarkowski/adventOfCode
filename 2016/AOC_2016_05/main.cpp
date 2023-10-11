#include <iostream>
#include <string>
#include <openssl/md5.h>

using namespace std;

string computeMD5(const string &input)
{
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char *)input.c_str(), input.length(), (unsigned char *)&digest);

    char mdString[33];
    for (int i = 0; i < 16; i++)
    {
        sprintf(&mdString[i * 2], "%02x", (unsigned int)digest[i]);
    }

    return mdString;
}

int main()
{
    string input = "ugkcyxxp";
    string password = "________";

    // int i = 0;
    // while (password.length() < 8)
    // {
    //     string hash = computeMD5(input + to_string(i));
    //     if (hash.substr(0, 5) == "00000")
    //     {
    //         password += hash[5];
    //         cout << password << endl;
    //     }
    //     i++;
    // }

    int i = 0;
    while (password.find("_") != string::npos)
    {
        string hash = computeMD5(input + to_string(i));
        if (hash.substr(0, 5) == "00000")
        {
            int position = hash[5] - '0';
            if (position >= 0 && position <= 7 && password[position] == '_')
            {
                password[position] = hash[6];
                cout << password << endl;
            }
        }
        i++;
    }

    cout << "Password: " << password << endl;
    return 0;
}

// g++ -o main main.cpp -L/opt/homebrew/opt/openssl@3/lib -lssl -lcrypto -I/opt/homebrew/opt/openssl@3/include
