int removeElement(int* nums, int numsSize, int val) {
    int notVal = 0;
    for(int i = 0; i< numsSize; i++){
        if(nums[i] != val){
            nums[notVal] = nums[i];
            notVal++;
        }
    }
    return notVal;
}