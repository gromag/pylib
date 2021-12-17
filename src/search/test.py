# afer loading tf.keras.datasets.cifar10.load_data() plot some sample images
def main():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)
    # plot some sample images
    for i in range(9):
        plt.subplot(330 + 1 + i)
        plt.imshow(x_train[i] cmap="coolwarm")


# reduce size of matrix by averaging inner dimension
