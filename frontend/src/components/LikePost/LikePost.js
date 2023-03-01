import { AiFillHeart } from '@react-icons/all-files/ai/AiFillHeart';
import { AiOutlineHeart } from '@react-icons/all-files/ai/AiOutlineHeart';


const LikeIcon = ({ state, color, size }) => {
    const Heart = state ? AiFillHeart : AiOutlineHeart;
    return (
      <Heart
        size={size}
        color={color}
        fill='currentColor'
        stroke='currentColor'
        style={{ cursor: 'pointer' }}
      />
    );
}


export const LikePost = ({ likes, handleReaction, isLiked, setShowModal }) => {
    const action = isLiked ? 'unlike' : 'like';
    const effect = isLiked ? 'negative' : 'positive';

    const handleClick = () => {
        handleReaction(action, effect, likes, 'isLiked');
      };
    return (
        <div
          className={`${
            isLiked ? 'reactions__block clicked--like' : 'reactions__block'
          }`}
        >
          <i
            onClick={handleClick}
            className={`${
              isLiked ? 'reactions__like reactions__liked' : 'reactions__like'
            }`}
          >
            <LikeIcon state={isLiked} size='2.5rem' />
          </i>
          <span>{likes && likes.length}</span>
        </div>
      );
}