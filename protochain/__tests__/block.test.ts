import {describe, test, expect} from '@jest/globals'
import Block from "../src/lib/block";

describe("Block tests", () => {

    test("Should be valid", () => {
        const block = new Block(1, "a", "block2")
        const valid = block.isValid();
        expect(valid).toBeTruthy();
    })

    test("Should NOT be valid (previous hash)", () => {
        const block = new Block(1, "", "block2");

        const valid = block.isValid();
        expect(valid).toBeFalsy();
    })

    test("Should NOT be valid (timestamp)", () => {
        const block = new Block(1, "abc", "block2");
        block.timestamp = 0;
        const valid = block.isValid();
        expect(valid).toBeFalsy();
    })

    test("Should NOT be valid (hash)", () => {
        const block = new Block(1, "abc", "block2");
        block.hash = ""
        const valid = block.isValid();
        expect(valid).toBeFalsy();
    })

    test("Should NOT be valid (data)", () => {
        const block = new Block(1, "abc", "");
        const valid = block.isValid();
        expect(valid).toBeFalsy();
    })

    test("Should NOT be valid (index)", () => {
        const block = new Block(-1, "a", "block2")
        const valid = block.isValid();
        expect(valid).toBeFalsy();
    })
})