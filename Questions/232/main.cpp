#include<iostream>

class MyQueue {
    std::deque<int> q;
    public: 
        MyQueue() {
        }

        void push(int x) {
            q.push_back(x);
        }

        int pop() {
            int ans = q.front();
            q.pop_front();
            return ans;
        }

        int peek() {
            return q.front();
        }

        bool empty() {
            return q.empty();
        }

};

int main() {
    MyQueue q = MyQueue();
    q.push(0);
    q.push(1);
    std::cout << q.pop() << std::endl;
    std::cout << q.peek() << std::endl;
    return 0;
}