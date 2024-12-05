/**
 * Block class
 */
export default class Block {
    index: number;
    hash: string;

    /**
     * Creates new block
     * @param index  the block index in blockchain
     * @param hash  the block hash
     */
    constructor(index: number, hash: string) {
        this.index = index;
        this.hash = hash
    }

    /**
     * Validates the block
     * @returns Return true if the block is valid
     */
    isValid(): boolean {
        if (this.index < 0) return false;
        if (!this.hash) return false;
        return true;

    }

}