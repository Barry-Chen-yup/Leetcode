class Solution {
public:
    bool canConstruct(string s, int k) {
        if (k > s.length()) {
            return false;
        }
        vector<int> char_count(26, 0);
        int ood_count = 0;

        for (char c : s){
            int index = c - 'a';
            char_count[index]++;
            if (char_count[index] % 2 == 1){
                ood_count++;
            }else{
                ood_count--;
            }
        }
        return ood_count <= k;
    }
};
