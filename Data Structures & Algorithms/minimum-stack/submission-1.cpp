class MinStack {

stack<int> stk;
stack<int> minstk;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);

        if(minstk.size())
        {
            if (minstk.top() >= val)
                minstk.push(val);
        } 
        else
        {
            minstk.push(val);
        }
    }
    
    void pop() {
        if (stk.top() == minstk.top())
            minstk.pop();
        stk.pop();
        
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minstk.top();
    }
};
