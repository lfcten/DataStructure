/**
 * Created by eb-pc on 2017/7/19.
 */

public class RBTree<T extends Comparable<T>> {

    private RBTNode<T> mRoot; // 根节点

    private static final boolean RED = false;
    private static final boolean BLACK = true;

    public class RBTNode<T extends Comparable<T>>{
        boolean color;            // 颜色
        T key;                    // 键值
        RBTNode<T> parent;        // 父节点
        RBTNode<T> left;          // 左孩子
        RBTNode<T> right;         // 右孩子
        public RBTNode(T key, boolean color, RBTNode<T> parent, RBTNode<T> left, RBTNode<T> right){
            this.key = key;
            this.color = color;
            this.parent = parent;
            this.left = left;
            this.right = right;
        }

        public T getKey(){
            return key;
        }

        public String toString(){
            return ""+key+(this.color==RED?"(R)":"(B)");
        }

    }

    public RBTree(){
        mRoot = null;
    }

    private RBTNode<T> parentOf(RBTNode<T> node){
        return node != null ? node.parent : null;
    }

    private boolean colorOf(RBTNode<T> node){
        return node != null ? node.color : BLACK;
    }

    private boolean isRed(RBTNode<T> node){
        return (node != null) && (node.color == RED);
    }

    private  boolean isBlack(RBTNode<T> node){
        return !isRed(node);
    }

    private void setRed(RBTNode<T> node){
        if (node != null){
            node.color = RED;
        }
    }

    private void setBlack(RBTNode<T> node){
        if (node != null){
            node.color = BLACK;
        }
    }

    private void setParent(RBTNode<T> node, RBTNode<T> parent){
        if (node != null){
            node.parent = parent;
        }
    }

    private void setColor(RBTNode<T> node, boolean color){
        if (node != null){
            node.color = color;
        }
    }

    private void leftRotate(RBTNode<T> x){
        RBTNode<T> y = x.right;
        x.right = y.left;
        if (y.left != null){
            y.left.parent = x;
        }
        y.parent = x.parent;
        if (x.parent == null){
            this.mRoot = y;
        }else{
            if (x.parent.left == x){
                x.parent.left = y;
            }
            else {
                x.parent.right = y;
            }
        }
        y.left = x;
        x.parent = y;
    }

    /*
     * 前序遍历"红黑树"
     */
    private void preOrder(RBTNode<T> node){
        if (node != null){
            System.out.printf(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    public void preOrder(){
        preOrder(mRoot);
    }

    /*
     * 中序遍历"红黑树"
     */
    private void inOrder(RBTNode<T> node){
        if (node != null){
            inOrder(node.left);
            System.out.printf(node.key + " ");
            inOrder(node.right);
        }
    }

    public void inOrder(){
        inOrder(mRoot);
    }

    /*
     * 后序遍历"红黑树"
     */
    private void postOrder(RBTNode<T> node){
        if (node != null){
            postOrder(node.left);
            postOrder(node.right);
            System.out.printf(node.key + " ");
        }
    }

    public void postOrder(){
        postOrder(mRoot);
    }

    /*
     * 查找键值为key的节点(递归实现)
     */
    private RBTNode<T> search(RBTNode<T> x, T key){
        if (x == null){
            return x;
        }
        int cmp = key.compareTo(x.key);
        if (cmp < 0){
            return search(x.left, key);
        }
        else if (cmp > 0){
            return search(x.right, key);
        } else {
            return x;
        }
    }

    public RBTNode<T> search(T key){
        return search(mRoot, key);
    }

    /*
     * (非递归)
     */
    private RBTNode<T> iterativeSearch(RBTNode<T> x, T key){
        while (x != null){
            int cmp = key.compareTo(x.key);
            if (cmp < 0){
                x = x.left;
            } else if (cmp > 0){
                x = x.right;
            }else {
                return x;
            }
        }
        return x;
    }

    public RBTNode<T> iterativeSearch(T key){
        return iterativeSearch(mRoot,key);
    }

    /*
     * 查找最小节点
     */
    private RBTNode<T> minimum(RBTNode<T> node){
        if (node == null){
            return null;
        }
        while (node.left != null){
            node = node.left;
        }
        return node;
    }

    public T minimum(){
        RBTNode<T> p = minimum(mRoot);
        if (p != null){
            return p.key;
        }
        return null;
    }

    /*
     * 查找最大节点
     */
    private RBTNode<T> maximun(RBTNode<T> node){
        if (node == null){
            return null;
        }
        while (node.right != null){
            node = node.right;
        }
        return node;
    }

    public T maximum(){
        RBTNode<T> p = maximun(mRoot);
        if (p != null){
            return p.key;
        }
        return null;
    }

    /*
     * 查找结点x的后继节点
     */
    public RBTNode<T> successor(RBTNode<T> x){
        if (x.right != null){
            return minimum(x.right);
        }
        RBTNode<T> y = x.parent;
        while((y != null) && (x == y.right)){
            x = y;
            y = y.parent;
        }
        return y;
    }

    /*
     * 查找节点x的前驱节点
     */
    public RBTNode<T>  predecessor(RBTNode<T> x){
        if (x.left != null){
            return maximun(x.left);
        }
        RBTNode<T> y = x.parent;
        while ((y != null) && x == y.left){
            x = y;
            y = y.parent;
        }
        return y;
    }

    /*
     * 右旋
     */
    private void rightRotate(RBTNode<T> x){
        RBTNode<T> y = x.left;
        x.left = y.right;
        if (y.right != null){
            y.right.parent = x;
        }
        y.parent = x.parent;
        if (y.parent == null){
            this.mRoot = y;
        }else{
            if (x == x.parent.left){
                x.parent.left = y;
            }
            else{
                x.parent.right = y;
            }
        }
        y.right = x;
        x.parent = y;
    }

    /*
     * 节点插入
     */
    private void insert(RBTNode<T> node){
        int cmp;
        RBTNode<T> y = null;
        RBTNode<T> x = this.mRoot;
        while (x != null){
            y = x;
            cmp = node.key.compareTo(x.key);

//            if (cmp == 0){
//                return;
//            }

            if (cmp < 0){
                x = x.left;
            }
            else {
                x = x.right;
            }
        }
        node.parent = y;
        if (y != null){
            cmp = node.key.compareTo(y.key);
            if (cmp < 0){
                y.left = node;
            }
            else {
                y.right = node;
            }
        }else{
            this.mRoot = node;
        }
        node.color = RED;
        inserFixUP(node);
    }

    public void insert(T key){
        RBTNode<T> node = new RBTNode<T>(key, BLACK, null,null,null);
        if (node != null){
            insert(node);
        }
    }

    private void inserFixUP(RBTNode<T> node){
        RBTNode<T> parent, gparent;

        while(((parent = parentOf(node))!=null) && isRed(parent)){
            gparent = parentOf(parent);
            if (parent == gparent.left){
                RBTNode<T> uncle = gparent.right;
                if ((uncle != null) && isRed(uncle)){
                    setBlack(uncle);
                    setBlack(parent);
                    setRed(gparent);
                    node = gparent;
                    continue;
                }
                if (parent.right == node){
                    RBTNode<T> tmp;
                    leftRotate(parent);
                    tmp = parent;
                    parent = node;
                    node = tmp;
                }
                setBlack(parent);
                setRed(gparent);
                rightRotate(gparent);
            }else{
                RBTNode<T> uncle = gparent.left;
                if ((uncle != null) && isRed(uncle)){
                    setBlack(parent);
                    setBlack(uncle);
                    setRed(gparent);
                    node = gparent;
                    continue;
                }
                if (parent.left==node){
                    RBTNode<T> tmp;
                    rightRotate(parent);
                    tmp = parent;
                    parent = node;
                    node = tmp;
                }
                setBlack(parent);
                setRed(gparent);
                leftRotate(gparent);
            }
        }
        setBlack(this.mRoot);
    }

    /*
     * 节点删除
     */
    private void remove(RBTNode<T> node){
        RBTNode<T> child, parent;
        boolean color;

        //左右孩子都不为空
        if ((node.left != null) && (node.right != null)){
            RBTNode<T> replace = successor(node);
            if (parentOf(node) != null){
                if (parentOf(node).left == node){
                    parentOf(node).left = replace;
                }
                else {
                    parentOf(node).right = replace;
                }
            }else{
             this.mRoot = replace;
            }
            child = replace.right;
            parent = parentOf(replace);
            color = colorOf(replace);
            if (parent == node){
                parent = replace;
            }else{
                if (child != null){
                    setParent(child, parent);
                }
                parent.left = child;
                replace.right = node.right;
                setParent(node.right, replace);
            }
            replace.parent = node.parent;
            replace.color = node.color;
            replace.left = node.left;
            node.left.parent = replace;
            if (color == BLACK){
                removeFixUP(child, parent);
            }
            node = null;
            return;
        }
        if (node.left != null){
            child = node.left;
        }else{
            child = node.right;
        }
        parent = node.parent;
        color = node.color;
        if (child != null){
            child.parent = parent;
        }
        if (parent != null){
            if (parent.left == node){
                parent.left = child;
            }
            else {
                parent.right = child;
            }
        }else {
            this.mRoot = child;
        }
        if (color == BLACK){
            removeFixUP(child, parent);
        }
        node = null;
    }

    public void remove(T key){
        RBTNode<T> node;

        if ((node = search(mRoot, key)) != null){
            remove(node);
        }
    }

    private void removeFixUP(RBTNode<T> node, RBTNode<T> parent){
        RBTNode<T> other;

        while ((node == null || isBlack(node))&& (node != this.mRoot)){
            if (parent.left == node){
                other = parent.right;
                // case1
                if (isRed(other)){
                    setBlack(other);
                    setRed(parent);
                    leftRotate(parent);
                    other = parent.right;
                }
                if ((other.left==null || isBlack(other.left)) && (other.right==null || isBlack(other.right))){
                    setRed(other);
                    node = parent;
                    parent = parentOf(node);
                }else {
                    if (other.right==null || isBlack(other.right)){
                        setBlack(other.left);
                        setRed(other);
                        rightRotate(other);
                        other = parent.right;
                    }
                    setColor(other,colorOf(parent));
                    setBlack(parent);
                    setBlack(other.right);
                    leftRotate(parent);
                    node = this.mRoot;
                    break;
                }
            }else {
                other = parent.left;
                if (isRed(other)){
                    setBlack(other);
                    setRed(parent);
                    rightRotate(parent);
                }else {
                    if (other.left==null || isBlack(other.left)){
                        setBlack(other.right);
                        setRed(other);
                        leftRotate(other);
                        other = parent.left;
                    }
                    setColor(other,colorOf(parent));
                    setBlack(parent);
                    setBlack(other.left);
                    rightRotate(parent);
                    node = this.mRoot;
                    break;
                }
            }
        }
    }

    private void destroy(RBTNode<T> tree){
        if (tree==null){
            return;
        }
        if (tree.left != null){
            destroy(tree.left);
        }
        if (tree.right != null){
            destroy(tree.right);
        }
        tree = null;
    }
    public void clear(){
        destroy(mRoot);
        mRoot = null;
    }

    private void print(RBTNode<T>tree, T key, int direction){
        if (tree!=null){
            if (direction==0){
                System.out.printf("%2d(B) is root\n", tree.key);
            }
            else{
                System.out.printf("%2d(%s) is %2d's %6s child\n", tree.key, isRed(tree)?"R":"B",key, direction==1?"right":"left");
            }
            print(tree.left,tree.key,-1);
            print(tree.right,tree.key,1);
        }
    }

    public void print(){
        if(mRoot != null){
            print(mRoot, mRoot.key, 0);
        }
    }

}
