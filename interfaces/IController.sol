// SPDX-License-Identifier: MIT
pragma solidity >=0.7.2;
pragma experimental ABIEncoderV2;

interface IController {
    enum ActionType {
        OpenVault, //0
        MintShortOption, //1
        BurnShortOption, //2
        DepositLongOption, //3
        WithdrawLongOption, //4
        DepositCollateral, //5
        WithdrawCollateral, //6
        SettleVault, //7
        Redeem, //8
        Call //9
    }

    struct ActionArgs {
        ActionType actionType;
        address owner;
        address secondAddress;
        address asset;
        uint256 vaultId;
        uint256 amount;
        uint256 index;
        bytes data;
    }

    struct Vault {
        address[] shortOtokens;
        address[] longOtokens;
        address[] collateralAssets;
        uint256[] shortAmounts;
        uint256[] longAmounts;
        uint256[] collateralAmounts;
    }

    function pool() external view returns (address);

    function whitelist() external view returns (address);

    function getPayout(address _otoken, uint256 _amount)
        external
        view
        returns (uint256);

    function operate(ActionArgs[] calldata _actions) external;

    function getAccountVaultCounter(address owner)
        external
        view
        returns (uint256);

    function oracle() external view returns (address);

    function getVault(address _owner, uint256 _vaultId)
        external
        view
        returns (Vault memory);

    function getProceed(address _owner, uint256 _vaultId)
        external
        view
        returns (uint256);

    function isSettlementAllowed(address otoken) external view returns (bool);
}
