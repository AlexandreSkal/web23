import sha256 from 'crypto-js/sha256'

/**
 * Block class
 */
export default class Block {
    index: number;
    timestamp: number;
    previousHash: string;
    hash: string;
    data: string;


    /**
     * Creates new block
     * @param index  the block index in blockchain
     * @param timestamp the block creation timestamp
     * @param previousHash the previous hash block
     * @param hash  the block hash
     * @param data the data information inside the current block
     */
    constructor(index: number, previousHash: string, data: string) {
        this.index = index;
        this.timestamp = Date.now();
        this.previousHash = previousHash;
        this.data = data;
        this.hash = this.getHash();

    }

    getHash(){
        return sha256(this.index + this.data + this.timestamp + this.previousHash).toString();
    }

    /**
     * Validates the block
     * @returns Return true if the block is valid
     */
    isValid(): boolean {
        if (this.index < 0) return false;
        if (!this.hash) return false;
        if (!this.previousHash) return false;
        if (this.timestamp < 1) return false;
        if (!this.data) return false;
        return true;

    }

}