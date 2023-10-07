# ERC721 +

Prototype to show ERC721 improvement that prevents the double minting of duplicates (exact same images) within a coillection.

ETHRome. October 2023.

## Installation

First ensure you are in a new and empty directory.

1. Create .env file and add environment variables, you can refer .env.example file

   ```javascript
   REACT_APP_COLOR_ADDRESS= // Contract address to interact, for testing you can use 0x320792c7a855B4fD0636df06014cd6f717fAfDeb
   REACT_APP_RPC_URL_1= // Your Infura RPC URL
   REACT_APP_RPC_URL_3= // Your Infura RPC URL
   REACT_APP_POLLING_INTERVAL= // Polling time interval, you can set it to 15000
   REACT_APP_INFURA_KEY= // Your Infura Key

   // Fortmatic Wallet
   REACT_APP_FORTMATIC_API_KEY= // Your Fortmatic Key
   REACT_APP_FORTMATIC_CHAIN_NAME= // Supported Fortmatic Network i.e, ropsten
   ```

3. Install dependencies and start project.

   ```javascript
   npm install
   npm run start
   ```

4. To build the application for production, use the build script. A production build will be in the `build` folder.
   ```javascript
   npm run build
   ```

#### Note:

If you want to use it with truffle, make sure you use `include-truffle` branch.
