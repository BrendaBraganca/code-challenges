int removeDuplicates(int* nums, int numsSize) {
    int* v2 = (int*) malloc(sizeof(int) * numsSize);
    v2[0] = nums[0];
    int acc = 0;
    int uni = 1;
    while(acc < (numsSize -1)){
        if(nums[acc] != nums [acc + 1]){
            v2[uni] = nums[acc+1];
            uni++;
        }
        acc++;
    }
    for(int i = 0; i < uni; i++){
        nums[i] = v2[i];
    }
    return uni; 
}