class Solution {
    stack<int> nums;

    string plus {"+"};
    string minus {"-"};
    string divide {"/"};
    string multiply {"*"};
    
    unordered_map<string, function<int(int, int)>> ops = {
        {plus, [](int a, int b){ return a + b; }}, 
        {minus, [](int a, int b){ return a - b; }}, 
        {divide, [](int a, int b){ return a / b; }}, 
        {multiply, [](int a, int b){ return a * b; }}, 
        }; 
    

public:
    int evalRPN(vector<string>& tokens) {

        for (auto elem : tokens){
            if(ops.count(elem) == 1)
            {
                int a = nums.top();
                nums.pop();
                int b = nums.top();
                nums.pop();
                int val = ops[elem](b, a);
                nums.push(val);
            }
            else
            {
                nums.push(stoi(elem));
            }
        }
        return nums.top();
    }

    
};
