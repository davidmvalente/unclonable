// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "Verifier_prova.sol";

contract UnclonableNFT is ERC721, ERC721URIStorage, Ownable {
    Verifier verifier;
    constructor(address initialOwner)
        ERC721("UnclonableNFT", "UNFT")
        Ownable(initialOwner)
    {
        verifier = new Verifier();
    }

    function safeMint(address to, string memory uri, 
            uint[2] memory a,
            uint[2][2] memory b,
            uint[2] memory c,
            uint[15] memory input
    )
        public
        onlyOwner
    {   
        if (verifier.verifyProof(a, b, c, input) == false) revert();
        _safeMint(to, input[0]);
        _setTokenURI(input[0], uri);
    }

    // The following functions are overrides required by Solidity.

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}