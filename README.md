# GA12-Opyn-Badger

The project is an attempt to show how one may use Opyn's contracts to mint a covered call that can then be sold on Gnosis Safe, Airswap, Uniswap, or Ox.

Initially I wanted to use Lyra to sell the call options but there was a slight hiccup in that dev process. Right now Lyra is deployed on Optimism and 
only accepts sUSD. If one was to start with wBTC they would need to swap for lUSD bridge to Optimism then swap to sUSD then buy/sell the options. While a 
viable method, testing for this flow would be difficult. I did not identify an end to end flow for testing so this route was dropped.

Running the code:

To run the code you will need a .env with an ETHERSCAN_TOKEN,WEB3_INFURA_PROJECT_ID, and PRIVATE_KEY defined. All addresses will need to be for kovan.

Make sure you change KovanWallet_addr in Openvault.py 



Things to be added:

Unit tests, integration tests, the ablity to sell the tokens in a test enviroment, integration with the badger strategy mix, diagrams showing the entire option flow.


Conclusion:
This was my first hackathon project, it was fun, seeing how development is done in web3 was interesting. Whoever solves the problem of getting new projects to clearly
document their code is going to change the game. If there are ways that this project could be improved, please let me know!
