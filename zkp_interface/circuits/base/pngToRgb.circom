pragma circom 2.0.0;

include "../node_modules/circomlib/circuits/bitify.circom";
include "../node_modules/circomlib/circuits/comparators.circom";
include "./poseidon2/poseidon2_hash.circom";


template FourBytesToUint() {
    signal input in[4];
    signal output out;
    
    component bytes_to_bits[4];
    bytes_to_bits[0] = Num2Bits(8);
    bytes_to_bits[1] = Num2Bits(8);
    bytes_to_bits[2] = Num2Bits(8);
    bytes_to_bits[3] = Num2Bits(8);
    
    bytes_to_bits[0].in <== in[3];
    bytes_to_bits[1].in <== in[2];
    bytes_to_bits[2].in <== in[1];
    bytes_to_bits[3].in <== in[0];

    component bits_to_num;
    bits_to_num = Bits2Num(32);
    for (var i = 0; i< 4; i++) {
        for (var j = 0; j < 8; j++) {
            bits_to_num.in[(i*8)+j] <== bytes_to_bits[i].out[j];
        }
    }
    out <== bits_to_num.out;
}

template PPMtoRGB(N, M, SIZE, HEADER_SIZE){
    signal input png_array[SIZE];
    signal input bitmap_array[N][M][3];    
    signal output hash;
    
    // verify signature
    var signature_size = 3;
    var signature[signature_size] = [80, 54, 10];

    for (var i = 0; i < signature_size; i++) {    
        png_array[i] === signature[i];
    }
    
    png_array[HEADER_SIZE+signature_size-1] === 10;
    
    var offset = HEADER_SIZE+signature_size;
    component equals[SIZE - offset];
    for (var i = 0; i < N; i++) {
        for (var j = 0; j < M; j++) {
            for (var k = 0; k < 3; k++) {
                equals[i*M*3+j*3+k] = IsEqual();
                equals[i*M*3+j*3+k].in[0] <== bitmap_array[i][j][k];
                equals[i*M*3+j*3+k].in[1] <== png_array[offset+i*M*3+j*3+k];
                0 === equals[i*M*3+j*3+k].out * (1-equals[i*M*3+j*3+k].out);


            }
        }
    }

    component poseidon = Poseidon2_hash(SIZE-offset);
    for (var j = 0; j < SIZE-offset; j++) {
        poseidon.inp[j] <== png_array[j+offset];
    }
    hash <== poseidon.out;
}

//MAIN component main {public [png_array] } = PPMtoRGB(Nt, Mt, SIZEt, HEADERt);