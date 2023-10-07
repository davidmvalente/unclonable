pragma circom 2.0.0;


template PNGtoRGB(N,M,SIZE,HEADER){
    signal input png_array[SIZE];
    signal output bitmap_array[N][M][3];
}

//MAIN component main {public [png_array, bitmap_array]} = PNGtoRGB(Nt,Mt,SIZEt,HEADERt);
