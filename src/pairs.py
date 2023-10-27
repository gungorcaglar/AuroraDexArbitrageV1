from web3 import Web3
import random

def choose():
    trisolaris = Web3.to_checksum_address("0x2CB45Edb4517d5947aFdE3BEAbF95A582506858B")
    wannaswap = Web3.to_checksum_address("0xa3a1ef5ae6561572023363862e238afa84c72ef5")
    auroraswap = Web3.to_checksum_address("0xA1B1742e9c32C7cAa9726d8204bD5715e3419861")

    routers = [
        trisolaris,
        wannaswap,
        auroraswap
    ]

    router1 = random.choice(routers)
    router2 = random.choice(routers)

    usdt = Web3.to_checksum_address("0x4988a896b1227218e4A686fdE5EabdcAbd91571f")

    base_pairs = [
        usdt
    ]

    base = random.choice(base_pairs)

    aurora = Web3.to_checksum_address("0x8BEc47865aDe3B172A928df8f990Bc7f2A3b9f79")
    wnear = Web3.to_checksum_address("0xC42C30aC6Cc15faC9bD938618BcaA1a1FaE8501d")
    tri = Web3.to_checksum_address("0xFa94348467f64D5A457F75F8bc40495D33c65aBB")
    dai = Web3.to_checksum_address("0xe3520349F477A5F6EB06107066048508498A291b")
    wbtc = Web3.to_checksum_address("0xF4eB217Ba2454613b15dBdea6e5f22276410e89e")
    usdc = Web3.to_checksum_address("0xB12BFcA5A55806AaF64E99521918A4bf0fC40802")
    xtri = Web3.to_checksum_address("0x802119e4e253D5C19aA06A5d567C5a41596D6803")
    avax = Web3.to_checksum_address("0x80A16016cC4A2E6a2CACA8a4a498b1699fF0f844")
    matic = Web3.to_checksum_address("0x6aB6d61428fde76768D7b45D8BFeec19c6eF91A8")
    bnb = Web3.to_checksum_address("0x2bF9b864cdc97b08B6D79ad4663e71B8aB65c45c")
    empyr = Web3.to_checksum_address("0xE9F226a228Eb58d408FdB94c3ED5A18AF6968fE1")
    flx = Web3.to_checksum_address("0xea62791aa682d455614eaA2A12Ba3d9A2fD197af")
    solace = Web3.to_checksum_address("0x501acE9c35E60f03A2af4d484f49F9B1EFde9f40")
    meta = Web3.to_checksum_address("0xc21Ff01229e982d7c8b8691163B0A3Cb8F357453")
    stNear = Web3.to_checksum_address("0x07F9F7f963C5cD2BBFFd30CcfB964Be114332E30")
    polar = Web3.to_checksum_address("0xf0f3b9Eee32b1F490A4b8720cf6F005d4aE9eA86")
    spolar = Web3.to_checksum_address("0x9D6fc90b25976E40adaD5A3EdD08af9ed7a21729")
    lunar = Web3.to_checksum_address("0x25e801Eb75859Ba4052C4ac4233ceC0264eaDF8c")
    orbital = Web3.to_checksum_address("0x3AC55eA8D2082fAbda674270cD2367dA96092889")
    ausdo = Web3.to_checksum_address("0x293074789b247cab05357b08052468B5d7A23c5a")
    bbt = Web3.to_checksum_address("0x4148d2Ce7816F0AE378d98b40eB3A7211E1fcF0D")
    usdtlp = Web3.to_checksum_address("0x5EB99863f7eFE88c447Bc9D52AA800421b1de6c9")
    aave = Web3.to_checksum_address("0x4e834cDCc911605227eedDDb89Fad336AB9dc00a")
    abr = Web3.to_checksum_address("0x2BAe00C8BC1868a5F7a216E881Bae9e662630111")
    abbusd = Web3.to_checksum_address("0x5C92A4A7f59A9484AFD79DbE251AD2380E589783")

    token_pairs = [
        wnear,
        aurora,
        tri,
        dai,
        wbtc,
        usdc,
        xtri,
        avax,
        matic,
        bnb,
        empyr,
        flx,
        solace,
        meta,
        stNear,
        polar,
        spolar,
        lunar,
        orbital,
        ausdo,
        bbt,
        usdtlp,
        aave,
        abr,
        abbusd
    ]

    token = random.choice(token_pairs)

    return router1, router2, base, token