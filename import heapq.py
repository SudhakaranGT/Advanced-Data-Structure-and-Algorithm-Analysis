import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_dict(text):
    frequency_dict = defaultdict(int)
    for char in text:
        frequency_dict[char] += 1
    return frequency_dict


def build_huffman_tree(frequency_dict):
    priority_queue = []
    for char, freq in frequency_dict.items():
        heapq.heappush(priority_queue, HuffmanNode(char, freq))

    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(priority_queue, merged_node)

    return heapq.heappop(priority_queue)


def build_huffman_codes(node, current_code, huffman_codes):
    if node.char:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)


def huffman_encoding(text):
    if len(text) == 0:
        return "", None

    frequency_dict = build_frequency_dict(text)
    huffman_tree = build_huffman_tree(frequency_dict)

    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, huffman_tree


def huffman_decoding(encoded_text, huffman_tree):
    if encoded_text == "" or huffman_tree is None:
        return ""

    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text


# Example usage
text = "Huffman coding is a data compression algorithm."
encoded_text, huffman_tree = huffman_encoding(text)
decoded_text = huffman_decoding(encoded_text, huffman_tree)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
