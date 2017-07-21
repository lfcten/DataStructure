import java.util.Scanner;

/**
 * Created by eb-pc on 2017/7/20.
 */
public class RBTreeTest {
    private static final int[] a = {10, 40, 30, 60, 90, 70, 20, 50, 80};
    private static final boolean mDebugInsert = false;
    private static final boolean mDebugDelete = false;
    public static void main(String[] args){
        int i, ilen = a.length;
        RBTree<Integer> tree = new RBTree<Integer>();
        System.out.printf("== 原始数据：");
        for(i=0;i<ilen;i++){
            System.out.printf("%d ",a[i]);
        }
        System.out.printf("\n");
        for(i=0;i<ilen;i++){
            tree.insert(a[i]);
            if(mDebugInsert){
                System.out.printf("==添加节点：%d\n",a[i]);
                System.out.printf("==树信息：\n");
                tree.print();
                System.out.printf("\n");
            }
        }
        System.out.printf("== 前序遍历: ");
        tree.preOrder();
        System.out.printf("\n== 中序遍历：");
        tree.inOrder();
        System.out.printf("\n== 后序遍历：");
        tree.postOrder();
        System.out.printf("\n");
        if(mDebugDelete) {
            for(i=0; i<ilen; i++){
                tree.remove(a[i]);
                System.out.printf("==删除节点：%d\n",a[i]);
                System.out.printf("树的信息：\n");
                tree.print();
                System.out.printf("\n");
            }
        }
        tree.clear();
    }
}
