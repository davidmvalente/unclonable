python3 zkp_interface/create_image.py
python3 zkp_interface/get_proof.py red_pixel.png zkp_interface/img/output.json
./zkp_interface/scripts/compile_circuit.sh zkp_interface/circuits/instances/pngToRgb.circom zkp_interface/img/output.json
./zkp_interface/scripts/proving_system/setup_prover.sh pngToRgb 18.ptau
./zkp_interface/scripts/proving_system/prover.sh pngToRgb
./zkp_interface/scripts/proving_system/verifier.sh pngToRgb --generate-contract unclonable_verifier
