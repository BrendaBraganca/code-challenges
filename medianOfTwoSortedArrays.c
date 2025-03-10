double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0;
    int j = 0;
    int acc = 0;
    int* nums3 = (int*) malloc(sizeof(int) * (nums1Size + nums2Size));

    while(i < nums1Size && j < nums2Size){
        if(nums1[i] <= nums2[j]){
            nums3[acc] = nums1[i];
            i++;
        } else {
            nums3[acc] = nums2[j];
            j++;
        }
        acc++;
    }

    if(i < nums1Size){
        while(i < nums1Size){
            nums3[acc] = nums1[i];
            i++;
            acc++;
        }
    } else {
        while( j < nums2Size){
            nums3[acc] = nums2[j];
            j++;
            acc++;
        }
    }
    if(acc %2 != 0){
        return nums3[acc/2];
    } 
    double result = (nums3[acc/2] + nums3[acc/2 - 1]);
    return result/2;
}