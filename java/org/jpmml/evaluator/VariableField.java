/*
 * Copyright (c) 2016 Villu Ruusmann
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

import java.util.Objects;

import org.dmg.pmml.DataType;
import org.dmg.pmml.Field;
import org.dmg.pmml.OpType;
import org.dmg.pmml.Visitor;
import org.dmg.pmml.VisitorAction;

class VariableField extends Field<VariableField> {

	private String name = null;


	private VariableField(){
	}

	VariableField(String name){
		setName(name);
	}

	@Override
	public String requireName(){
		return getName();
	}

	@Override
	public String getName(){
		return this.name;
	}

	@Override
	public VariableField setName(String name){
		this.name = Objects.requireNonNull(name);

		return this;
	}

	@Override
	public String getDisplayName(){
		return null;
	}

	@Override
	public VariableField setDisplayName(String displayName){
		throw new UnsupportedOperationException();
	}

	@Override
	public OpType requireOpType(){
		return getOpType();
	}

	@Override
	public OpType getOpType(){
		String name = getName();

		throw new MissingFieldException(name);
	}

	@Override
	public VariableField setOpType(OpType opType){
		throw new UnsupportedOperationException();
	}

	@Override
	public DataType requireDataType(){
		return getDataType();
	}

	@Override
	public DataType getDataType(){
		String name = getName();

		throw new MissingFieldException(name);
	}

	@Override
	public VariableField setDataType(DataType dataType){
		throw new UnsupportedOperationException();
	}

	@Override
	public VisitorAction accept(Visitor visitor){
		throw new UnsupportedOperationException();
	}
}