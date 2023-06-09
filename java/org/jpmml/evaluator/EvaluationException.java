/*
 * Copyright (c) 2014 Villu Ruusmann
 *
 * This file is part of JPMML-Evaluator
 *
 * JPMML-Evaluator is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * JPMML-Evaluator is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with JPMML-Evaluator.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.jpmml.evaluator;

import org.dmg.pmml.PMMLObject;
import org.jpmml.model.PMMLException;

/**
 * <p>
 * Thrown to indicate an abrupt termination of the evaluation operation.
 * </p>
 */
public class EvaluationException extends PMMLException {

	public EvaluationException(String message){
		super(message);
	}

	public EvaluationException(String message, PMMLObject context){
		super(message, context);
	}

	static
	public String formatName(String name){
		return format(name);
	}

	static
	public String formatKey(Object object){
		return format(object);
	}

	static
	public String formatValue(Object object){

		if(object instanceof FieldValue){
			FieldValue fieldValue = (FieldValue)object;

			object = fieldValue.getValue();
		}

		return format(object);
	}

	static
	public String format(Object object){

		if(object instanceof String){
			String string = (String)object;

			return "\"" + string + "\"";
		}

		return (object != null ? String.valueOf(object) : null);
	}
}
