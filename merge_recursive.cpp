#include <iostream>
#include <vector>
using namespace std;

// Phiên bản Iterative (Two Pointers) - ban đầu
void mergeIterative(const vector<int>& a, const vector<int>& b) {
    int i = 0, j = 0;
    int n = a.size(), m = b.size();
    vector<int> c;

    while (i < n || j < m) {
        if (j == m || (i < n && a[i] <= b[j]))
            c.push_back(a[i++]);
        else
            c.push_back(b[j++]);
    }

    cout << "Iterative result: ";
    for (auto it : c)
        cout << it << " ";
    cout << endl;
}

// Phiên bản Recursive - tối ưu hóa
void mergeRecursiveHelper(const vector<int>& a, const vector<int>& b, 
                         vector<int>& result, int i, int j) {
    // Base cases
    if (i >= a.size() && j >= b.size()) 
        return;
    
    if (i >= a.size()) {
        // Copy remaining elements from b
        result.push_back(b[j]);
        mergeRecursiveHelper(a, b, result, i, j + 1);
        return;
    }
    
    if (j >= b.size()) {
        // Copy remaining elements from a
        result.push_back(a[i]);
        mergeRecursiveHelper(a, b, result, i + 1, j);
        return;
    }
    
    // Recursive case: compare and choose smaller element
    if (a[i] <= b[j]) {
        result.push_back(a[i]);
        mergeRecursiveHelper(a, b, result, i + 1, j);
    } else {
        result.push_back(b[j]);
        mergeRecursiveHelper(a, b, result, i, j + 1);
    }
}

void mergeRecursive(const vector<int>& a, const vector<int>& b) {
    vector<int> result;
    mergeRecursiveHelper(a, b, result, 0, 0);
    
    cout << "Recursive result: ";
    for (auto it : result)
        cout << it << " ";
    cout << endl;
}

// Phiên bản Recursive tối ưu hơn - Divide and Conquer
vector<int> mergeRecursiveDivideConquer(const vector<int>& a, const vector<int>& b) {
    // Base cases
    if (a.empty()) return b;
    if (b.empty()) return a;
    
    vector<int> result;
    
    if (a[0] <= b[0]) {
        result.push_back(a[0]);
        vector<int> subA(a.begin() + 1, a.end());
        vector<int> merged = mergeRecursiveDivideConquer(subA, b);
        result.insert(result.end(), merged.begin(), merged.end());
    } else {
        result.push_back(b[0]);
        vector<int> subB(b.begin() + 1, b.end());
        vector<int> merged = mergeRecursiveDivideConquer(a, subB);
        result.insert(result.end(), merged.begin(), merged.end());
    }
    
    return result;
}

void printDivideConquerResult(const vector<int>& a, const vector<int>& b) {
    vector<int> result = mergeRecursiveDivideConquer(a, b);
    cout << "Divide & Conquer result: ";
    for (auto it : result)
        cout << it << " ";
    cout << endl;
}

// Đo thời gian thực thi
#include <chrono>

void benchmarkMethods(const vector<int>& a, const vector<int>& b) {
    using namespace chrono;
    
    // Test Iterative
    auto start = high_resolution_clock::now();
    mergeIterative(a, b);
    auto end = high_resolution_clock::now();
    auto iterativeTime = duration_cast<microseconds>(end - start);
    
    // Test Recursive Helper
    start = high_resolution_clock::now();
    mergeRecursive(a, b);
    end = high_resolution_clock::now();
    auto recursiveTime = duration_cast<microseconds>(end - start);
    
    // Test Divide & Conquer
    start = high_resolution_clock::now();
    printDivideConquerResult(a, b);
    end = high_resolution_clock::now();
    auto divideConquerTime = duration_cast<microseconds>(end - start);
    
    cout << "\n=== PERFORMANCE COMPARISON ===" << endl;
    cout << "Iterative: " << iterativeTime.count() << " microseconds" << endl;
    cout << "Recursive: " << recursiveTime.count() << " microseconds" << endl;
    cout << "Divide & Conquer: " << divideConquerTime.count() << " microseconds" << endl;
}

int main() {
    vector<int> a = {1, 3, 5, 7, 9, 11};
    vector<int> b = {2, 4, 6, 8, 10, 12};
    
    cout << "Array A: ";
    for (auto x : a) cout << x << " ";
    cout << "\nArray B: ";
    for (auto x : b) cout << x << " ";
    cout << "\n\n";
    
    // So sánh các phương pháp
    benchmarkMethods(a, b);
    
    return 0;
}