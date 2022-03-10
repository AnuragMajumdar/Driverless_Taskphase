class operations:

    def determinantOfMatrix(mat, n):

        temp = [0] * n
        total = 1
        det = 1

        for i in range(0, n):
            index = i

            while (mat[index][i] == 0 and index < n):
                index += 1

            if (index == n):
                continue

            if (index != i):

                for j in range(0, n):
                    mat[index][j], mat[i][j] = mat[i][j], mat[index][j]

                det = det * int(pow(-1, index - i))

            for j in range(0, n):
                temp[j] = mat[i][j]

            for j in range(i + 1, n):
                num1 = temp[i]
                num2 = mat[j][i]

                for k in range(0, n):

                    mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])

                total = total * num1
        for i in range(0, n):
            det = det * mat[i][i]

        return int(det / total)

    if __name__ == "__main__":

        mat = [[1, 0, 2, -1], [3, 0, 4, 5], [2, 1, 4, -3], [1, 6, 5, 0]]
        N = len(mat)

        print("Determinant:", determinantOfMatrix(mat, N))