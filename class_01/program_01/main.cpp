// Implement a simple binary tree

#include <iostream>
using namespace std;

class Node {
 public:
  int value;
  Node* left;
  Node* right;

 public:
  Node(int value) {
    this->value = value;
    left = nullptr;
    right = nullptr;
  }
};

class BinaryTree {
 public:
  Node* root;
  BinaryTree(int value) { root = new Node(value); }
  void inorder(Node* node) {
    if (node != nullptr) {
      inorder(node->left);
      cout << node->value << " ";
      inorder(node->right);
    }
  }
  void preorder(Node* node) {
    if (node != nullptr) {
      cout << node->value << " ";
      preorder(node->left);
      preorder(node->right);
    }
  }
  void postorder(Node* node) {
    if (node != nullptr) {
      postorder(node->left);
      postorder(node->right);
      cout << node->value << " ";
    }
  }
};

int main() {
  BinaryTree tree(1);
  tree.root->left = new Node(2);
  tree.root->right = new Node(3);
  tree.root->left->left = new Node(4);
  tree.root->left->right = new Node(5);
  tree.root->right->left = new Node(6);
  tree.root->right->right = new Node(7);

  cout << "Inorder Traversal: ";
  tree.inorder(tree.root);
  cout << endl;

  cout << "Preorder Traversal: ";
  tree.preorder(tree.root);
  cout << endl;

  cout << "Postorder Traversal: ";
  tree.postorder(tree.root);
  cout << endl;
}

/*
Inorder Traversal: 4 2 5 1 6 3 7
Preorder Traversal: 1 2 4 5 3 6 7
Postorder Traversal: 4 5 2 6 7 3 1
*/